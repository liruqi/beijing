from BeautifulSoup import BeautifulSoup
import urllib2
import re
import subprocess
import os

htmlfile = open("audit_house_list/index.html")
html_page = htmlfile.read()
soup = BeautifulSoup(html_page)
for link in soup.findAll('a'):
    href = link.get('href')
    hid = href.split("=")[-1]
    localname = "audit_house_detail/raw/" + hid + ".html"
    if os.path.exists(localname):
        print "exists: " + hid
	continue
    if os.path.exists("audit_house_detail/audit_house_detail.aspx?House_Id=" + hid):
        os.rename("audit_house_detail/audit_house_detail.aspx?House_Id=" + hid, localname)
        print "rename: " + hid
	continue
    localf = open(localname, "w")
    httpf = urllib2.urlopen(href)
    localf.write(httpf.read())
    httpf.close()
    localf.close()
    print href


