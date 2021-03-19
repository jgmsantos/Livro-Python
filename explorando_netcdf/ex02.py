import xarray as xr

# Abertura do arquivo NetCDF.
ds = xr.open_dataset('../dados/netcdf/prec.2020.nc', decode_times=False)

print('=====================================')
print('Informações sobre a dimensão latitude')
print(ds.lat)

print('=====================================')
print('Informações sobre a dimensão longitude')
print(ds.lon)

print('=====================================')
print('Informações sobre a dimensão tempo')
print(ds.time)


