# install html-xml-utils
# http://stackoverflow.com/questions/7334942

# OS detect: http://stackoverflow.com/questions/394230/

SED_I=" -i"
case "$OSTYPE" in
  darwin*)  
    echo "OSX"
    brew install html-xml-utils #For OS X
    SED_I=" -i '.back'"
    ;; 
  *) 
    echo "unknown: $OSTYPE"
    apt-get install html-xml-utils #For Debian
    ;;
esac

mkdir audit_house_detail

RAWDIR=audit_house_list/`date +"%Y-%m-%d"`
if [ ! -d $RAWDIR ]; then 
mkdir -p $RAWDIR

for i in {1..366}
do
    FILENAME=$RAWDIR"/p${i}.html"
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
""" > "${RAWDIR}.html"

for i in {1..366}
do
    FILENAME="audit_house_list/i${i}.html"
    cat $FILENAME >> "${RAWDIR}.html"
done

echo "</tbody></table></body></html>" >> "${RAWDIR}.html"
# replace <img border="0" height="16" src="http://210.75.213.188/shh/portal/bjjs/images/icon_show.gif" width="16"/> with "detail"
sed $SED_I 's#<img border="0" height="16" src="http://210.75.213.188/shh/portal/bjjs/images/icon_show.gif" width="16"/>#detail#g' "${RAWDIR}.html"

sudo pip install BeautifulSoup
python parse-table.py --input "${RAWDIR}.html"
