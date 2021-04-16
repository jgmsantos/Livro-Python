import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
import cartopy.feature as cfeature
from cartopy import config
from netCDF4 import Dataset as nc
from cartopy.feature import NaturalEarthFeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

# Área de interesse.
LonW=-90
LonE=-30
LatS=-60.0
LatN=10.0

# Abertura dos arquivos.
fu = nc('../../../dados/netcdf/uwnd.nc')
fv = nc('../../../dados/netcdf/vwnd.nc')

# Importação das variáveis.
u = fu.variables['uwnd'][0,0,:,:]
v = fv.variables['vwnd'][0,0,:,:]

vel = np.sqrt(u ** 2 + v ** 2)  # Calcula a velocidade do vento (m/s).

lats = fu.variables['lat'][:]
lons = fu.variables['lon'][:]

ax = plt.axes(projection=ccrs.PlateCarree())

# Criação do mapa com a divisão dos estados brasileiros.
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

# Plot da variável.
plt.contourf(lons, lats, vel, 60, transform=ccrs.PlateCarree())

# Título principal da figura e tamanho.
plt.title('Vento em 1000hPa', fontsize=6)

# Formatação do eixo x e tamanho.
plt.xlabel('Longitude', fontsize=6)  # Define o tamanho do título do eixo x.
plt.xticks(fontsize=6)  # Define o tamanho dos rótulos do eixo x.

# Formatação do eixo y e tamanho.
plt.ylabel('Latitude', fontsize=6)  # Define o tamanho do título do eixo y.
plt.yticks(fontsize=6)  # Define o tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

# Gera a barra de corres, format = formata os valores, shrink = tamanho da barra de cores, orientation = orientação da barra, 
# pad = proximidade do eixo x inferior.
cbar = plt.colorbar(ax=ax, format='%.0f', shrink=0.65, orientation='horizontal', pad=0.17)
cbar.ax.tick_params(labelsize=6)  # Tamanho dos rótulos da barra de cores.
cbar.set_label('('r'$m.s^{-1}$'')', fontsize=6)  # Unidade da barra de cores.

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex04.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)