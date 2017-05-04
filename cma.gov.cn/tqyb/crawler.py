# install html-xml-utils
# http://www.cma.gov.cn/tqyb/images/forecast/products/yuntu/l/sevp_nsmc_wxcl_asc_fff_achn_ffff_py_201606122345fffff.jpg
# http://image.nmc.cn/product/2017/05/04/WXCL/medium/SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_20170504081500000.JPG?v=1493886889694

import datetime
import time
import httplib
import os
import errno

now = int (time.time()) - 8 * 3600
now = (now / 15 / 60 ) * 15 * 60

host = "image.nmc.cn"
RAWDIR = os.path.dirname(os.path.abspath(__file__)) + "/../" + host + "/product"

conn = httplib.HTTPConnection(host, 80)
for i in range(365):
    ts = now - 15 * 60 * i
    dt = datetime.datetime.fromtimestamp(ts)
    year = dt.strftime('%Y') 
    month = dt.strftime('%m') 
    dayIM = dt.strftime('%d') 
    tm = dt.strftime('%Y%m%d%H%M') 
    localname=RAWDIR + "/%s/%s/%s/WXCL/medium/SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_%s00000.JPG" % (year, month, dayIM, tm) 
    FILEURI="/product/%s/%s/%s/WXCL/medium/SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_%s00000.JPG" % (year, month, dayIM, tm)

    print "get: " + FILEURI
    conn.request('GET', FILEURI)
    httpf = conn.getresponse()
    body = httpf.read()
    if (len(body) > 1020):
        try:
            os.makedirs(os.path.dirname(localname))
        except OSError as exc:
            if exc.errno == errno.EEXIST:
                pass
            else:
                raise
        localf = open(localname, "w")
        localf.write(body)
        localf.close()
        print FILEURI

    httpf.close()

