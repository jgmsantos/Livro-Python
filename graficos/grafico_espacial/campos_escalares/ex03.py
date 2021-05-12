import proplot as plot
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
from cartopy.feature import NaturalEarthFeature


# Abertura do arquivo NetCDF.
dsu = xr.open_dataset('../../../dados/netcdf/uwnd.nc')
dsv = xr.open_dataset('../../../dados/netcdf/vwnd.nc')

#print(ds)  # Informações sobre o arquivo.

# Importando variáveis.
u = dsu['uwnd'][0,0,:,:]  # (time, level, lat, lon)
v = dsv['vwnd'][0,0,:,:]  # (time, level, lat, lon)
vel = np.sqrt(u ** 2 + v ** 2)  # Calcula a velocidade do vento (m/s).
lat = dsu['lat']
lon = dsu['lon']

# Linhas do continente/estados do Brasil.
estados = NaturalEarthFeature(category="cultural", scale="50m", facecolor="none",
          name="admin_1_states_provinces_shp")

fig, ax = plot.subplots(axwidth=5, tight=True, proj='pcarree',)

# Formatação do mapa.
ax.format(coast=True, borders=True, innerborders=True,
          labels=True, grid=True, latlines=10, lonlines=5,
          latlim=(-60, 10), lonlim=(-90, -30))

# Título da figura.
plt.title('Vento Meridional em 1000 hPa', fontsize=15)

# Plot da variável.
map = ax.contourf(lon, lat, vel, cmap='Spectral', 
                  levels=plot.arange(2, 10, 1), extend='both')

#  Adiciona a barra de cores.
x = fig.colorbar(map, loc='r', shrink=0.95, orientation='vertical')
plt.tick_params(labelsize=13)  # Tamanho da fonte da barra de cores.
x.set_label('Velocidade (m/s)', fontsize=13)  # Unidade da barra de cores.

# Adiciona o contorno dos estados e países.
ax.add_feature(estados, linewidth=0.5, edgecolor="k")

# Salva a figura no formato ".jpg" com dpi=300.
fig.save('ex03.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)