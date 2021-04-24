import geopandas as gp
import rioxarray
import xarray as xr
from shapely.geometry import mapping
#import matplotlib.pyplot as plt
#import numpy as np
#import cartopy.io.shapereader as shpreader
#import cartopy.crs as ccrs
#import matplotlib.ticker as mticker
#from cartopy.feature import ShapelyFeature

# Abertura do arquivo NetCDF.
ds = xr.open_dataset('../dados/netcdf/GPCP.nc')

# Converte a longitude do formato 0-360 para -180 a +180.
ds.coords['lon'] = ((ds.coords['lon'] + 180) % 360) - 180
ds = ds.sortby(ds.lon)

# Importa as dimensões do arquivo de precipitação.
ds.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
ds.rio.write_crs("epsg:4329", inplace=True)

# Abertura do arquivo shapefile do Brasil.
Shape_Brasil = gp.read_file('../dados/shapefile/brasil/Brasil.shp', 
                            crs="epsg:4329")

# Aplica a máscara do Brasil sobre o dado de precipitação.
prec_mask = ds.rio.clip(Shape_Brasil.geometry.apply(mapping), 
                        Shape_Brasil.crs, 
                        drop=False) 

#fig = plt.figure(figsize=(10, 8))

## Cria um eixo e sua projeção.
#ax = fig.add_subplot(111, projection=ccrs.PlateCarree())
#
## Seleciona o primeiro tempo e visualiza a variável. O plt.contour representa apenas o contorno.
## O plt.contourf, o campo preenchido.
##ax.contourf(ds['lon'], ds['lat'], ds['precip'][0,:,:])
## Plot da temperatura do ar.
##im = ax.contourf(ds['lon'], ds['lat'], ds['precip'][0,:,:], 
##                 levels=np.arange(0, 20, 2), cmap='coolwarm',
##                 transform=ccrs.PlateCarree(), extend='both')
#
#im = ax.contourf(prec_mask['lon'], prec_mask['lat'], prec_mask['precip'][0,:,:], 
#                 levels=np.arange(0, 20, 2), cmap='coolwarm',
#                 transform=ccrs.PlateCarree(), extend='both')
#
## Adiciona o shapefile do Brasil ao mapa.
#shape_estados_brasil = ShapelyFeature(shpreader.Reader('../dados/shapefile/brasil/Brasil.shp').geometries(), ccrs.PlateCarree(), facecolor='none', edgecolor='black', linewidth=0.5)
#
#ax.add_feature(shape_estados_brasil)
#
#g1 = ax.gridlines(crs=ccrs.PlateCarree(), linestyle='--', color='gray', draw_labels=True)
#g1.xlocator = mticker.FixedLocator(list(np.arange(-80, -30, 5)))
#g1.ylocator = mticker.FixedLocator(list(np.arange(-30, 5, 5)))
#g1.right_labels = False
#g1.top_labels = False
#g1.xlabel_style = {'size': 17}
#g1.ylabel_style = {'size': 17}
#
## Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
#plt.savefig('ex01b.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)#