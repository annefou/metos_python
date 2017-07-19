import netCDF4
import numpy as np

f = netCDF4.Dataset('orography.nc', 'w')
f.createDimension('time', None)
f.createDimension('z', 3)
f.createDimension('y', 4)
f.createDimension('x', 5)
lats = f.createVariable('lat', float, ('y',), zlib=True)
lons = f.createVariable('lon', float, ('x',), zlib=True)
orography = f.createVariable('orog', float, ('y', 'x'), zlib=True, least_significant_digit=1, fill_value=0)
lat_out  = [60, 65, 70, 75]
lon_out  = [ 30,  60,  90, 120, 150]
# Create field values for orography
data_out = np.arange(4*5) # 1d array but with dimension x*y
data_out.shape = (4,5) # reshape to 2d array
orography[:] = data_out
lats[:] = lat_out
lons[:] = lon_out
f.close()