import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib
import matplotlib.pyplot as plt
import xarray as xr

font = {"family": "normal", "weight": "normal", "size": 16}

matplotlib.rc("font", **font)

## Lendo o dataset criado no ex01.py (sempre verifique o nome do arquivo!)
ds = xr.open_dataset("gfs.0p25.2018022000.f036.nc")

fig = plt.figure(figsize=(12, 10))
ax = plt.axes(projection=ccrs.PlateCarree())

# Adiciona os contornos estaduais, com resolução de 50m, a partir da base NaturalEarth (https://www.naturalearthdata.com/).
states_provinces = cfeature.NaturalEarthFeature(
    category="cultural",
    name="admin_1_states_provinces_lines",
    scale="50m",
    facecolor="none",
)

ax.add_feature(states_provinces, edgecolor="k")

## Fazendo o plot
ds["Wind_speed_gust_surface"].plot(ax=ax, cmap="jet")

## Salvando a figura
fig.savefig("ex02.png", dpi=300, bbox_inches="tight")
