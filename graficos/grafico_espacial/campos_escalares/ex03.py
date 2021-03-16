# Manipulação de dados
import geopandas as gpd
import pandas as pd 
import rioxarray
import xarray as xr
import numpy as np
# Mapas
import matplotlib.pyplot as plt
import cartopy, cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.colors as colors
# Paleta de cores
import cmocean

# Abertura do arquivo.
dataset = xr.open_dataset('../../../dados/netcdf/PREC.IMERG.2019.pantanal.nc', decode_times=False)
dataset.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
dataset.rio.write_crs("epsg:4326", inplace=True)
dataset.rio.write_grid_mapping(inplace=True)

# Abertura do arquivo shapefile dos biomas.
shapefile = gpd.read_file("../../../dados/shapefile/biomas/Biomas5000.shp", crs="epsg:4326")

# Importação da variável de interesse.
dataset.sel(time=0.0)['prec'].plot()

# Seleção do bioma de interesse.
shape = shapefile[shapefile['COD_BIOMA'] == "PTN"]
shape['geometry'].plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
shapefile = gpd.read_file("../../../dados/shapefile/brasil/Brasil.shp", crs="epsg:4326")

# leitura shapefile estados BR
shapefile = gpd.read_file("../../../dados/shapefile/brasil/Brasil.shp", crs="epsg:4326")

# Título de cada figura.
title = [['Janeiro', 'Fevereiro', 'Março', 'Abril'],
         ['Maio', 'Junho', 'Julho', 'Agosto'],
         ['Setembro', 'Outubro', 'Novembro', 'Dezembro']]

# Array de datas (0.0 = janeiro, ..., 11.0 = dezembro).
yyyymmdd = [['0.0', '1.0', '2.0', '3.0'],
            ['4.0', '5.0', '6.0', '7.0'],
            ['8.0', '9.0', '10.0', '11.0']] 
            
# altere para nrows 4 para os 12 meses
fig, axes = plt.subplots(nrows=3, ncols=4, figsize=(13, 13), gridspec_kw = {'wspace':0.05, 'hspace':0.13}, subplot_kw={'projection': ccrs.PlateCarree()})

for lin in [0, 1, 2]:
    for col in [0, 1, 2, 3]:
        # se precisar montar outros paineis, basta alterar o dataset de entrada
        figure = dataset['prec'].sel(time=yyyymmdd[lin][col]).plot.pcolormesh(
            ax=axes[lin,col], robust=True, norm=colors.Normalize(vmin=0, vmax=300), cmap='RdYlBu',
            add_colorbar=False, levels=13, add_labels=False)
        axes[lin,col].add_feature(cfeature.COASTLINE)
        # Adiciona título dos meses.
        axes[lin,col].set_title(title[lin][col], fontsize=18, ha='center')
        # Adiciona o contorno dos estados em cinza.
        axes[lin,col].add_geometries(shapefile.geometry, crs=ccrs.PlateCarree(), facecolor='none', edgecolor='gray', linewidth=0.55)
        # Adiciona contorno do Pantanal em preto.
        axes[lin,col].add_geometries(shape.geometry, crs=ccrs.PlateCarree(), facecolor='none', edgecolor='k', linewidth=2.5)       
        axes[lin,col].add_feature(cfeature.BORDERS)

# Adiciona o cbar.
cbar_ax = fig.add_axes([0.90, 0.25, 0.02, 0.60])
cbar = fig.colorbar(figure, cax=cbar_ax, pad=0.009, ticks=np.arange(0,325,25), orientation='vertical')
cbar.ax.tick_params(labelsize=15) 

# adiciona titulo ao painel
plt.suptitle('Precipitação 2019', fontsize=20, ha='center', y=1, x = 0.53)
fig.subplots_adjust(top=0.95)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex03.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)