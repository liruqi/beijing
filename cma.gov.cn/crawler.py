# Create by Ruqi Li (liruqi@gmail.com)
# All rights reserved.

# install html-xml-utils
# http://www.cma.gov.cn/tqyb/images/forecast/products/yuntu/l/sevp_nsmc_wxcl_asc_fff_achn_ffff_py_201606122345fffff.jpg
# http://image.nmc.cn/product/2017/05/04/WXCL/medium/SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_20170504081500000.JPG?v=1493886889694

import datetime
import time
import httplib
import os
import errno


now = int (time.time())
now = (now / 30 / 60 ) * 30 * 60 + (15 * 60)
utc_now_dt = datetime.datetime.fromtimestamp(now - 13 * 3600)
print utc_now_dt

host = "image.nmc.cn"
RAWDIR = os.path.dirname(os.path.abspath(__file__)) + "/../" + host + "/product"

image_dir = RAWDIR + "/%s/%s/%s/WXCL/medium" % (utc_now_dt.strftime('%Y') , utc_now_dt.strftime('%m'), utc_now_dt.strftime('%d')) 
chinapedia_nephogram = open('/tmp/chinapedia_nephogram', 'w+')
chinapedia_nephogram.write(image_dir + '\n')
chinapedia_nephogram.write("%s_%s_%s" % (utc_now_dt.strftime('%Y') , utc_now_dt.strftime('%m'), utc_now_dt.strftime('%d')) + '\n')
chinapedia_nephogram.close()

conn = httplib.HTTPConnection(host, 80)
for i in range(48 * 3):
    ts = now - 30 * 60 * i
    dt = datetime.datetime.fromtimestamp(ts)
    utc_dt = datetime.datetime.fromtimestamp(ts - 8 * 3600)
    year = dt.strftime('%Y') 
    month = dt.strftime('%m') 
    dayIM = dt.strftime('%d') 
    tm = utc_dt.strftime('%Y%m%d%H%M') 
    localname=RAWDIR + "/%s/%s/%s/WXCL/medium/SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_%s00000.JPG" % (year, month, dayIM, tm) 
    FILEURI="/product/%s/%s/%s/WXCL/medium/SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_%s00000.JPG" % (year, month, dayIM, tm)
    
    if os.path.exists(localname):
        print ('Exists', i, ': ' + FILEURI)
        break
    print "get: " + FILEURI
    conn.request('GET', FILEURI)
    httpf = conn.getresponse()
    body = httpf.read()
    if (len(body) > 13782):
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
    else:
        print "failed: " + FILEURI
    httpf.close()

