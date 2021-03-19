from netCDF4 import Dataset as nc 

# Abertura do arquivo NetCDF.
ds = nc('../dados/netcdf/prec.2020.nc', mode='r')

print(ds.variables.keys())  # dict_keys(['time', 'lon', 'lat', 'prec'])

print('==========================================')
print(ds.variables)