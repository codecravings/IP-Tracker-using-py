import pygeoip

gip = pygeoip.GeoIP("GeoLiteCity.dat")
res = gip.record_by_addr('66.249.64.1')
for key, val in res.items():
    print('%s : %s' % (key, val))
