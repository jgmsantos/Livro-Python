import xclim
import xarray as xr

#Abertura do arquivo com o xarray.
ds = xr.open_dataset('../dados/netcdf/tmed_serie.nc')

# Dado 1D => time=31, lat=1, lon=1
temp = ds['TEMP2m'][:,0,0]  

num_dias = xclim.atmos.maximum_consecutive_warm_days(temp, thresh = '30 C', freq = 'MS')

# Total de dias: 7.
print(f'Total de dias: {int(num_dias)}.')