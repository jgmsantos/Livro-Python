import matplotlib.pyplot as plt
import xarray as xr
from matplotlib.cm import get_cmap
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.feature import NaturalEarthFeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import numpy as np

# Área de interesse.
LonW=-75
LonE=-43
LatS=-17.75
LatN=5.75

fig, ax = plt.subplots(figsize=(3,3), subplot_kw={'projection': ccrs.PlateCarree()}, ncols=1, nrows=1)

# Criação do mapa com as divisão dos estados brasileiro.
ax.set_global()
ax.coastlines(linewidth=1.0, color='black')
ax.add_feature(cfeature.BORDERS, linestyle='-', linewidth=1.0, edgecolor='black')
ax.spines['geo'].set_linewidth(0.5)
ax.tick_params(width=0.5)

# Define os rótulos dos eixos e bordas do mapa.
ax.tick_params(direction='out', length=6, width=1.0, colors='black', grid_color='black', grid_alpha=0.0)
ax.set_xticks(np.linspace(LonW, LonE, 5), crs=ccrs.PlateCarree())
ax.set_yticks(np.linspace(LatS, LatN, 6), crs=ccrs.PlateCarree())
ax.set_extent([LonW, LonE, LatS, LatN], crs=ccrs.PlateCarree())

lon_formatter = LongitudeFormatter(number_format='.0f', degree_symbol='', dateline_direction_label=False)
lat_formatter = LatitudeFormatter(number_format='.0f', degree_symbol='') 
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)

states = NaturalEarthFeature(category='cultural', scale='50m', facecolor='none', name='admin_1_states_provinces_shp')
ax.add_feature(states, edgecolor='black', linestyle='-', linewidth=0.5)

# Abertura do arquivo com o xarray.
ds = xr.open_dataset('../../../dados/netcdf/TMED.CPTEC.CLIMA.amazonia.nc', decode_times=False)

plot = ds.tmed[0,:,:].plot.contourf(levels=[25, 25.5, 26, 26.5, 27, 27.5, 28, 28.5, 29], ax=ax, transform=ccrs.PlateCarree(), cmap='jet', vmin=25, vmax=29, add_colorbar=False)

#  Título principal da figura e tamanho.
plt.title('Temperatura no bioma Amazônia', fontsize=8)

#  Formatação do eixo x e tamanho.
plt.xlabel('Longitude', fontsize=7)  #  Define o tamanho do título do eixo x.
plt.xticks(fontsize=7)  #  Define o tamanho dos rótulos do eixo x.

#  Formatação do eixo y e tamanho.
plt.ylabel('Latitude', fontsize=7)  #  Define o tamanho do título do eixo y.
plt.yticks(fontsize=7)  #  Define o tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  #  Habilita o tickmark do eixo direito.

cbaxes1 = fig.add_axes([0.01, 0.11, 0.95, 0.05]) 
cbar = fig.colorbar(plot, cax=cbaxes1, drawedges=True, orientation='horizontal')
cbar.ax.tick_params(labelsize=7)

plt.subplots_adjust(left=None, bottom=0.3, right=None, top=None, wspace=None, hspace=None)

#  Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex01.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)