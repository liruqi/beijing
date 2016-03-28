from BeautifulSoup import BeautifulSoup
import urllib2
import re
import subprocess
import os
import httplib
import argparse
import sys

parser = argparse.ArgumentParser(description='Automatically crawl transaction detail page')
parser.add_argument('--input', dest='input', default="audit_house_list/index.html", help='Input html. If not set "audit_house_list/index.html" will be used')
args = parser.parse_args(sys.argv[1:])

htmlfile = open(args.input)
html_page = htmlfile.read()
soup = BeautifulSoup(html_page)

conn = httplib.HTTPConnection("210.75.213.188", 80)

for link in soup.findAll('a'):
    href = link.get('href')
    hid = href.split("=")[-1]
    localname = "audit_house_detail/raw/" + hid + ".html"
    if os.path.exists(localname):
        print "exists: " + hid
	if os.path.exists("audit_house_detail/audit_house_detail.aspx?House_Id=" + hid):
            print "remove dup: " + hid
            os.rename("audit_house_detail/audit_house_detail.aspx?House_Id=" + hid, "/tmp/" + hid + ".html")
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


