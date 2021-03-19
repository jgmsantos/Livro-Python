import xarray as xr

# Abertura do arquivo NetCDF.
ds = xr.open_dataset('../dados/netcdf/prec.2020.nc', decode_times=False)

print('=====================================')
print('Informações sobre a variável')
print(ds.prec)