from BeautifulSoup import BeautifulSoup
import urllib2
import re
import subprocess
import os
import httplib

htmlfile = open("audit_house_list/index.html")
html_page = htmlfile.read()
soup = BeautifulSoup(html_page)

conn = httplib.HTTPConnection("210.75.213.188", 80)

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
    print "get: " + href.split("http://210.75.213.188")[1]
    conn.request('GET', href.split("http://210.75.213.188")[1])
    httpf = conn.getresponse()
    localf.write(httpf.read())
    httpf.close()
    localf.close()
    print href


