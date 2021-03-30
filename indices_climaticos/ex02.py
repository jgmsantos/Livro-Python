import xclim
import xarray as xr

# Abertura do arquivo com o xarray.
ds = xr.open_dataset('../dados/netcdf/GPCP.serie.nc')

# Dado 1D => time=31, lat=1, lon=1
prec = ds['precip'][:,0,0]  

# Importação da variável do arquivo.
num_dias = xclim.indices._threshold.dry_days(prec, thresh = '3.0 mm/day', freq = 'MS')

# Total de dias: 8.
print(f'Total de dias: {int(num_dias)}.')

#num_dias = xclim.indicators.atmos.maximum_consecutive_dry_days(prec, thresh = '2 mm/day', freq = 'MS')

# Total de dias: 1.
#print(f'Total de dias: {int(num_dias)}.')

# Importação da variável do arquivo.
#x = xclim.indices._threshold.dry_days(ds['precip'][:,0,0], thresh = '2.0 mm/day', freq = 'YS')

# https://xclim.readthedocs.io/en/stable/indicators_api.html#xclim.indicators.atmos.dry_days
# Temperatura.
# https://xclim.readthedocs.io/en/stable/notebooks/example.html#Threshold-indices

#print(help(xclim.indices._threshold.dry_days))