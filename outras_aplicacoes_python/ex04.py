import cartopy.crs as crs
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
from cartopy.feature import NaturalEarthFeature
from py3grads import Grads

# Carregando ambiente GrADS.
ga = Grads(verbose=False)

#  Lendo arquivo descritor.
ga("open wrf2022021700/WRF_cpt_05KM_2022021700.ctl")

# Obtendo o tempo inicial da previsão.
ga("set t 1")
time = ga("q time")
stime = list(time[0])[0].split()[2]

# Obtendo o tempo 73 (isto é, 72h de previsão).
ga("set t 73")
time = ga("q time")
ctime = list(time[0])[0].split()[4]

# Definindo as fronteiras estaduais e da costa.
states = NaturalEarthFeature(
    category="cultural",
    scale="50m",
    facecolor="none",
    name="admin_1_states_provinces_shp",
)

# Tabela de cores do NWS (https://unidata.github.io/python-gallery/examples/Precipitation_Map.html).
clevs = [
    0,
    1,
    2.5,
    5,
    7.5,
    10,
    15,
    20,
    30,
    40,
    50,
    70,
    100,
    150,
    200,
    250,
    300,
    400,
    500,
    600,
    750,
]
cmap_data = [
    (1.0, 1.0, 1.0),
    (0.3137255012989044, 0.8156862854957581, 0.8156862854957581),
    (0.0, 1.0, 1.0),
    (0.0, 0.8784313797950745, 0.501960813999176),
    (0.0, 0.7529411911964417, 0.0),
    (0.501960813999176, 0.8784313797950745, 0.0),
    (1.0, 1.0, 0.0),
    (1.0, 0.6274510025978088, 0.0),
    (1.0, 0.0, 0.0),
    (1.0, 0.125490203499794, 0.501960813999176),
    (0.9411764740943909, 0.250980406999588, 1.0),
    (0.501960813999176, 0.125490203499794, 1.0),
    (0.250980406999588, 0.250980406999588, 1.0),
    (0.125490203499794, 0.125490203499794, 0.501960813999176),
    (0.125490203499794, 0.125490203499794, 0.125490203499794),
    (0.501960813999176, 0.501960813999176, 0.501960813999176),
    (0.8784313797950745, 0.8784313797950745, 0.8784313797950745),
    (0.9333333373069763, 0.8313725590705872, 0.7372549176216125),
    (0.8549019694328308, 0.6509804129600525, 0.47058823704719543),
    (0.6274510025978088, 0.42352941632270813, 0.23529411852359772),
    (0.4000000059604645, 0.20000000298023224, 0.0),
]
cmap = mcolors.ListedColormap(cmap_data, "precipitation")
norm = mcolors.BoundaryNorm(clevs, cmap.N)

# Configuração da figura.
plt.close("all")
fig, ax = plt.subplots(
    1, 1, figsize=(10, 10), subplot_kw={"projection": crs.PlateCarree()}
)

# Plot para o domínio completo da previsão.
lons = ga.exp("lon")
lats = ga.exp("lat")

# Plot com zoom sobre sudeste brasileiro.
# Opção 1: Definir zoom diretamente pelo GrADS (mais rápido, pois carrega na memória apenas os dados da área selecionada)
# ga(f"set lon {360-55} {360-36}") # Longitudes 55°W e 36°W convertida para padrão 0 a 360°, respectivamente.
# ga('set lat -30 -12')
# lons = ga.exp('lon')
# lats = ga.exp('lat')

# Opção 2: Definir a extensão da área no próprio plot.
# ax.set_extent([-55,-36,-30,-12]) # limites das coordenadas oeste, leste, sul, norte

# Gerando o plot.
apcp = ga.exp("APCPsfc")
cf = ax.contourf(lons, lats, apcp, clevs, cmap=cmap, norm=norm, latlon=True)
ax.set_title("WRF 5km CPTEC/INPE", fontsize=16, loc="left")
ax.set_title(f"{stime} a {ctime}", fontsize=16, loc="right")

cb = plt.colorbar(cf, ax=ax, pad=0.01, shrink=0.8)
cb.set_label("Precipitação acumulada [mm]", fontsize=16)

# Adicionando shapefile dos estados e linhas costeiras.
ax.add_feature(states, linewidth=1.5, edgecolor="black")
ax.coastlines("10m", linewidth=0.8, color="black")

plt.tight_layout()
plt.show()
fig.savefig("ex04.png", dpi=300, bbox_inches="tight", pad_inches=0.03)
