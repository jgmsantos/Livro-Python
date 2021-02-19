import matplotlib.pyplot as plt
import xarray as xr
from matplotlib.cm import get_cmap
from cartopy.feature import ShapelyFeature
import cartopy.io.shapereader as shpreader
import cartopy.crs as ccrs

fig, ax = plt.subplots(figsize=(3,3))  #  Define o tamanho da figura.
ax = plt.axes(projection=ccrs.PlateCarree())

# Abertura do arquivo com o xarray.
ds = xr.open_dataset('../../../dados/netcdf/TMED.CPTEC.CLIMA.amazonia.nc', decode_times=False)

# Abertura do arquivo shapefile.
shape_bioma_amazonia = ShapelyFeature(shpreader.Reader('../../../dados/shapefile/bioma_amazonia/amazonia.shp').geometries(), ccrs.PlateCarree(), facecolor='none', edgecolor='black', linewidth=1.0)
shape_estados_brasil = ShapelyFeature(shpreader.Reader('../../../dados/shapefile/brasil/Brasil.shp').geometries(), ccrs.PlateCarree(), facecolor='none', edgecolor='black', linewidth=0.5)

# Adiciona o shapefile ao mapa.
ax.add_feature(shape_bioma_amazonia)
ax.add_feature(shape_estados_brasil)

# Seleciona o primeiro tempo e visualiza a variável. O plt.contour representa apenas o contorno.
# O plt.contourf, o campo preenchido.
plt.contour(ds['lon'], ds['lat'], ds['tmed'][0,:,:], colors="black", linestyles='solid', linewidths=0.5, levels=[25, 25.5, 26, 26.5, 27, 27.5, 28, 28.5, 29])
plt.contourf(ds['lon'], ds['lat'], ds['tmed'][0,:,:], cmap=get_cmap("jet"), levels=[25, 25.5, 26, 26.5, 27, 27.5, 28, 28.5, 29])

# Título principal da figura e tamanho.
plt.title('Temperatura no bioma Amazônia', fontsize=8)

# Formatação do eixo x e tamanho.
plt.xlabel('Longitude', fontsize=7)  # Define o tamanho do título do eixo x.
plt.xticks(fontsize=7)  # Define o tamanho dos rótulos do eixo x.

# Formatação do eixo y e tamanho.
plt.ylabel('Latitude', fontsize=7)  # Define o tamanho do título do eixo y.
plt.yticks(fontsize=7)  # Define o tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

# Gera a barra de corres, sua orientação, proximidade (pad) do eixo x inferior e valores de temperatura definidos pelo usuário.
cbar = plt.colorbar(ax = ax, shrink=0.98, orientation='horizontal', pad=0.03, ticks=[25, 25.5, 26, 26.5, 27, 27.5, 28, 28.5, 29])
cbar.ax.tick_params(labelsize=6)  # Tamanho dos rótulos da barra de cores.

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex02.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)