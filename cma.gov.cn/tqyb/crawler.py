# install html-xml-utils
# http://www.cma.gov.cn/tqyb/images/forecast/products/yuntu/l/sevp_nsmc_wxcl_asc_fff_achn_ffff_py_201606122345fffff.jpg
# 201606121545

import datetime
import time
import httplib
import os

now = int (time.time()) - 8 * 3600
now = (now / 15 / 60 ) * 15 * 60

RAWDIR = os.path.dirname(os.path.abspath(__file__)) + "/images/forecast/products/yuntu/l"


conn = httplib.HTTPConnection("www.cma.gov.cn", 80)
for i in range(365):
    ts = now - 15 * 60 * i
    dt = datetime.datetime.fromtimestamp(ts)
    tm = dt.strftime('%Y%m%d%H%M') 
    localname=RAWDIR + "/sevp_nsmc_wxcl_asc_fff_achn_ffff_py_%sfffff.jpg" % (tm) 
    FILEURI="/tqyb/images/forecast/products/yuntu/l/sevp_nsmc_wxcl_asc_fff_achn_ffff_py_%sfffff.jpg" % (tm)

    print "get: " + FILEURI
    conn.request('GET', FILEURI)
    httpf = conn.getresponse()
    body = httpf.read()
    if (len(body) > 500):
        localf = open(localname, "w")
        localf.write(body)
        localf.close()
        print FILEURI

    httpf.close()

