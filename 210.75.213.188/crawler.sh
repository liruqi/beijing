# install html-xml-utils
# http://stackoverflow.com/questions/7334942
brew install html-xml-utils
mkdir audit_house_detail

if [ ! -d audit_house_list ]; then 
mkdir audit_house_list

for i in {1..366}
do
    FILENAME="audit_house_list/p${i}.html"
# or curl -o 
    wget -k -O $FILENAME "http://210.75.213.188/shh/portal/bjjs/audit_house_list.aspx?pagenumber=${i}&pagesize=20"
    hxnormalize -l 240 -x $FILENAME 2>/dev/null | hxselect -s '\n' -c "table.houseList tbody" > "audit_house_list/i${i}.html"
done
fi

echo """<!DOCTYPE HTML>
<html lang="zh-Hans">
<head>
<meta charset="UTF-8">
</head>
<body>
<table>
<thead>
<tr>
<th width="60">核验编号</th>
<th width="60">区县</th>
<th width="100">小区名称</th>
<th width="80">户型</th>
<th width="60">面积</th>
<th width="60">拟售价格</th>
<th width="120">发布机构</th>
<th width="70">时间</th>
<th width="50">详细</th>
</tr>
</thead><tbody>
""" > "audit_house_list/index.html"

for i in {1..366}
do
    FILENAME="audit_house_list/i${i}.html"
    cat $FILENAME >> "audit_house_list/index.html"
done

echo "</tbody></table></body></html>" >> "audit_house_list/index.html"
// replace <img border="0" height="16" src="http://210.75.213.188/shh/portal/bjjs/images/icon_show.gif" width="16"/> with 详情
# sudo pip install BeautifulSoup
python parse-table.py > list.txt
cat list.txt | sort -n | uniq > audit_house_detail/index.txt

# download file audit_house_detail/index.txt
 
