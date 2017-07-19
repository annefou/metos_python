import netCDF4
import numpy as np

f = netCDF4.Dataset('orography.nc', 'r')
lats = f.variables['lat']
lons = f.variables['lon']
orography = f.variables['orog']
print(lats[:])
print(lons[:])
print(orography[:])
f.close()