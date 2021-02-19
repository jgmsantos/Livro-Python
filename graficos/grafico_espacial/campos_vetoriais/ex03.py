import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.feature import NaturalEarthFeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import numpy as np

# Área de interesse.
LonW=-90
LonE=-30
LatS=-60.0
LatN=10.0

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

#  Abertura do arquivo com o xarray.
dsu = xr.open_dataset('../../../dados/netcdf/uwnd.nc')
dsv = xr.open_dataset('../../../dados/netcdf/vwnd.nc')

#  Importando variáveis.
u = dsu['uwnd'][0,9,:,:]
v = dsv['vwnd'][0,9,:,:]
vel = np.sqrt(u*u + v*v)  # Calcula a velocidade do vento (m/s).
lat = dsu['lat']
lon = dsu['lon']

#  Plota o vetor do vento e sua magnitude (vel). headwidth = tamanho da ponta do vetor, headlength = comprimento da ponta do vetor, 
#  color = cor dos vetores.
vetor = plt.quiver(lon, lat, u, v, vel, headwidth=6, headlength=6, color='black', scale=8, scale_units='xy')

#  Posição x, y onde desenhar o vetor, 30 = unidade (m/s) que representa o vetor, r'$30 \frac{m}{s}$' = texto que vai aparecer na 
#  figura, labelpos = em qual posição do vetor deve-se adicionar o label, coordinates = qual eixo deve-se inserir o label.
vetorkey = plt.quiverkey(vetor, 0.67, 0.9, 30, r'$30m.s^{-1}$', labelpos='E', coordinates='figure', labelsep=0.02, fontproperties=dict(size=4))
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

#  Título principal da figura e tamanho.
plt.title('Vento em 200hPa', fontsize=6)

#  Formatação do eixo x e tamanho.
plt.xlabel('Longitude', fontsize=5)  #  Define o tamanho do título do eixo x.
plt.xticks(fontsize=5)  #  Define o tamanho dos rótulos do eixo x.

#  Formatação do eixo y e tamanho.
plt.ylabel('Latitude', fontsize=5)  #  Define o tamanho do título do eixo y.
plt.yticks(fontsize=5)  #  Define o tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  #  Habilita o tickmark do eixo direito.

#  Gera a barra de corres, format = formata os valores, shrink = tamanho da barra de cores, orientation = orientação da barra, 
#  pad = proximidade do eixo x inferior.
cbar = plt.colorbar(ax=ax, format='%.0f', shrink=0.65, orientation='horizontal', pad=0.17)
cbar.ax.tick_params(labelsize=4)  # Tamanho dos rótulos da barra de cores.
cbar.set_label('('r'$m.s^{-1}$'')', fontsize=4)  #  Unidade da barra de cores.

#  Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex03.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)