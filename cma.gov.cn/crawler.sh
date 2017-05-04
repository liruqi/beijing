# install html-xml-utils

TODAY=`date +"%Y-%m-%d"`

python crawler.py 

git add --all images
git commit -m "Update nephogram for $TODAY"
git push

