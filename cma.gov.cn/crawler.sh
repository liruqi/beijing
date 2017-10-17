# install html-xml-utils

TODAY=`date +"%Y-%m-%d"`

python crawler.py >> /tmp/chinapedia_nephogram.log 

git add --all ../image.nmc.cn
git commit -m "Update nephogram for $TODAY"
git push


cd `head -n 1 /tmp/chinapedia_nephogram`
ffmpeg -framerate 1 -pattern_type glob -i '*.JPG' -i /root/china.mp3 -codec copy -c:v libx264 -r 30 -pix_fmt yuv420p -t 48 /srv/http/chinapedia.org/nephogram/`tail -n 1 /tmp/chinapedia_nephogram`.mp4
cd -

