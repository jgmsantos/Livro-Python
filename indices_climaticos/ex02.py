import xclim
import xarray as xr

#Abertura do arquivo com o xarray.
ds = xr.open_dataset('../dados/netcdf/GPCP.serie.nc')

# Dado 1D => time=31, lat=1, lon=1
prec = ds['precip'][:,0,0]  

num_dias = xclim.atmos.maximum_consecutive_dry_days(prec, thresh = '2 mm/day', freq = 'MS')

# Total de dias: 1.
print(f'Total de dias: {int(num_dias)}.')

#https://xclim.readthedocs.io/en/stable/indicators_api.html#xclim.indicators.atmos.dry_days
#https://xclim.readthedocs.io/en/stable/notebooks/example.html#Threshold-indices