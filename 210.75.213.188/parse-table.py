from BeautifulSoup import BeautifulSoup
import urllib2
import re

htmlfile = open("audit_house_list/index.html")
html_page = htmlfile.read()
soup = BeautifulSoup(html_page)
for link in soup.findAll('a'):
    print link.get('href')

