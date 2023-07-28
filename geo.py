import os
import pandas as pd
from ctypes import cdll

from geosupport import Geosupport, GeosupportError


# Geocode addresses 



g = Geosupport()
def geocode(input):
    # collect inputs
    uid = input.pop('uid')
    hnum = input.pop('house_number')
    sname = input.pop('street_name')
    borough = input.pop('borough')

    try:
        geo1 = g['AP'](street_name=sname, house_number=hnum, borough=borough, mode='regular')
        geo2 = g['1B'](street_name=sname, house_number=hnum, borough=borough, mode='regular')
        geo2.pop('Longitude')
        geo2.pop('Latitude')
        geo = {**geo1, **geo2}
        geo = parse_output(geo)
        geo.update(dict(uid=uid, mode='regular', func='AP+1B', status='success'))

    except GeosupportError:
        try:
            geo = g['1B'](street_name=sname, house_number=hnum, borough=borough, mode='tpad')
            geo = parse_output(geo)
            geo.update(dict(uid=uid, mode='tpad', func='1B', status='success'))

        except GeosupportError as e:
            geo = parse_output(e.result)
            geo.update(uid=uid, mode='tpad', func='1B', status='failure')
print(geocode('475 Riverside Drive, New York City, New York'))

with Pool(processes=cpu_count()) as pool:
        it = pool.map(geocode, records, 10000)