import geopandas as gp
import rioxarray
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import mapping


# Abertura do arquivo NetCDF.
ds = xr.open_dataset('../dados/netcdf/GPCP.nc')

# Converte longitude do formato 0-360 a -180 a +180.
ds.coords['lon'] = ((ds.coords['lon'] + 180) % 360) - 180
ds = ds.sortby(ds.lon)

# Importa as dimensões do arquivo de precipitação.
ds.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
ds.rio.write_crs("epsg:4329", inplace=True)

# Abertura do arquivo shapefile do Brasil.
Shape_Brasil = gp.read_file('../dados/shapefile/brasil/Brasil.shp', crs="epsg:4329")

# Aplica a máscara do Brasil sobre o dado de precipitação.
prec_mask = ds.rio.clip(Shape_Brasil.geometry.apply(mapping), Shape_Brasil.crs, drop=False) 

y = prec_mask.mean(dim=('lon', 'lat'))

# Opções de personalização do NetCDF.
# Precip é o nome da variável do arquivo NetCDF.
encoding1={'precip': {'_FillValue': -999, 
                      'complevel': 9, 
                      'zlib': True},
           'time': {'zlib': False, '_FillValue': None},
           'lat': {'zlib': False, '_FillValue': None},
           'lon': {'zlib': False, '_FillValue': None}}

# Salva o resultado no NetCDF.
prec_mask.to_netcdf(path='Precipitacao_Brasil.nc', 
                    unlimited_dims={'time':True}, 
                    encoding=encoding1)