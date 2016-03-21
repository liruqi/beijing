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
<table>""" > "audit_house_list/index.html"

for i in {1..366}
do
    FILENAME="audit_house_list/i${i}.html"
    cat $FILENAME >> "audit_house_list/index.html"
done

echo "</table></body></html>" >> "audit_house_list/index.html"

# sudo pip install BeautifulSoup
python parse-table.py > list.txt
cat list.txt | sort -n | uniq > list-uniq.txt

# download file list-uniq.txt
 
