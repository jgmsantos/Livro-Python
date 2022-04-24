# Realiza a importação das bibliotecas necessárias.
import numpy as np
import cartopy
import cartopy.crs as ccrs
from cartopy.feature import NaturalEarthFeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import matplotlib.pyplot as plt

# Importa recursos necessÁrios para interpolar os dados de estação.
from scipy.interpolate import griddata

# Carrega as variáveis em listas.
lat, lon, temp = np.loadtxt(
    "../dados/texto/data_station.dat", usecols=(1, 2, 3), unpack=True
)

# Define os limites da grade do mapa.
lonLeft = np.min(lon) - 0.5
lonRight = np.max(lon) + 0.5
latLow = np.min(lat) - 0.95
latTop = np.max(lat) + 0.95

Lat_Labels = np.linspace(latLow, latTop, 6)
Lon_Labels = np.linspace(lonLeft, lonRight, 6)

# Criando eixos de mapas.
ax = plt.axes(projection=ccrs.PlateCarree())

# Ajusta o mapa na regiao de interesse.
ax.set_extent([lonLeft, lonRight, latLow, latTop], crs=cartopy.crs.PlateCarree())

# Plota a máscara de continente e oceano.
ax.coastlines(linewidth=0.25)
ax.add_feature(cartopy.feature.LAND, facecolor="gainsboro", edgecolor="none")
ax.add_feature(cartopy.feature.OCEAN, facecolor="lightsteelblue", edgecolor="none")

# Plota as linhas dos estados.
states = NaturalEarthFeature(
    category="cultural", scale="10m", facecolor="none", name="admin_1_states_provinces"
)
ax.add_feature(states, edgecolor="black", linestyle="-", linewidth=0.25)

# Define o formato dos labelas dos eixos x e y.
ax.set_xticks(Lon_Labels, crs=ccrs.PlateCarree())
ax.set_yticks(Lat_Labels, crs=ccrs.PlateCarree())
lon_formatter = LongitudeFormatter(
    number_format=".0f", degree_symbol="°", dateline_direction_label=True
)
lat_formatter = LatitudeFormatter(number_format=".0f", degree_symbol="°")
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
ax.set_xlabel("")
ax.set_ylabel("")

# Plota os labels com os valores da variável.
plt.scatter(lon, lat, c="k", s=30)
plt.scatter(lon, lat, c=temp, s=20, cmap="RdYlGn_r")
for label, xpt, ypt in zip(temp, lon, lat):
    plt.text(xpt - 0.06, ypt + 0.06, label)

# Plota a barra de cores e o título.
plt.colorbar()

plt.title("Temperatura Máxima em 06-02-2018")
plt.tight_layout()
plt.savefig("ex01.tif", bbox_inches="tight")
