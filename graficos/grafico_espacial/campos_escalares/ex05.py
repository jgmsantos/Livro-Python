import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import cartopy.feature as cfeature
import cartopy.crs as ccrs
import matplotlib.ticker as mticker
from cartopy.feature import ShapelyFeature
from cartopy.io.shapereader import Reader


# Abertura do arquivo com o xarray.
ds = xr.open_dataset('../../../dados/netcdf/tmed.clima.amazonia.nc', decode_times=False)

tmed = ds.tmed[0,:,:]  # Define o primeiro tempo a ser plotado.
lon = tmed.lon  # Importa as coordenadas de longitude.
lat = tmed.lat # Importa as coordenadas de latitude.

fig = plt.figure(figsize=(10, 8))

# Cria um eixo e sua projeção.
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())

# Domínio espacial de interesse. LonW, LonE, LatS, LatN.
ax.set_extent([-75, -43, -17, 6])

# Plot da temperatura do ar.
im = ax.contourf(lon, lat, tmed, 
                 levels=np.arange(25, 29.5, 0.5), cmap='coolwarm',
                 transform=ccrs.PlateCarree(), extend='both')

# Abertura do arquivo shapefile do bioma Amazônia.
shape_feature = ShapelyFeature(Reader('../../../dados/shapefile/bioma_amazonia/amazonia.shp').geometries(),
                                ccrs.PlateCarree(), facecolor='none')

# Adiciona o contorno do bioma Amazônia.
ax.add_feature(shape_feature, edgecolor='black', linestyle='-', lw=3)

# Adiciona o contorno do continente.
ax.add_feature(cfeature.COASTLINE)

# Adiciona o limite dos países.
ax.add_feature(cfeature.BORDERS)

# Adiciona o limite dos estados.
states = cfeature.NaturalEarthFeature(category='cultural',
                                      name='admin_1_states_provinces_shp',
                                      scale='50m',
                                      facecolor='none')

# Formatação dos limites dos estados.
ax.add_feature(states, edgecolor='black', linestyle='-')

# Insere a barra de cores.
cbar = plt.colorbar(im, ax=ax, pad=0.08, fraction=0.055, orientation='horizontal')
cbar.set_label(label='Temperatura ($\degree$C)', size=17)
cbar.ax.tick_params(labelsize=17)

# Adiciona título a figura.
ax.set_title('Temperatura do ar no bioma Amazônia', fontsize=18)

# Adiciona linhas de grade horizontal e vertical ao mapa.
g1 = ax.gridlines(crs=ccrs.PlateCarree(), linestyle='--', color='gray', draw_labels=True)
# Intervalo dos rótulos dos eixos x e y.
g1.xlocator = mticker.FixedLocator(list(np.arange(-75, -45, 5)))
g1.ylocator = mticker.FixedLocator(list(np.arange(-20, 10, 5)))

# Tamanho da fonte dos rótulos dos eixos x e y. 
g1.xlabel_style = {'size': 17}
g1.ylabel_style = {'size': 17}

# Remove os rótulos dos topo e da direita do mapa.
g1.right_labels = False
g1.top_labels = False

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
fig.savefig('ex05.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)