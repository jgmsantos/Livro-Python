import cartopy.crs as crs
import proplot as plot
import xarray as xr
from cartopy.feature import ShapelyFeature
from cartopy.io.shapereader import Reader

# Abertura do arquivo NetCDF.
ds = xr.open_dataset("../../../dados/netcdf/RF.nc")

# print(ds)  # Informações sobre o arquivo.

# Valores de risco de fogo.
valores_de_rf = [0, 0.15, 0.40, 0.70, 0.95, 1]
# (0+0.15)/2=0.075; (0.15+0.40)/2=0.275; (0.40+0.70)/2=0.55;
# (0.70+0.95)/2=0.825; (0.95+1)/2=0.975.
posicao_categoria = [0.075, 0.275, 0.55, 0.82, 0.975]
categorias_de_rf = ["Mínimo", "Baixo", "Médio", "Alto", "Crítico"]

# Cores de interesse. Sempre número de valores + 1, ou seja, 5 + 1 = 6 cores.
cores = ["green", "vivid green", "yellow", "orange", "red"]

# Definição da área de interesse.
variavel = ds.sel(lat=slice(-25, -2), lon=slice(-61, -41))

# Linhas do contorno do bioma.
bioma = ShapelyFeature(
    Reader(
        "../../../dados/shapefile/bioma_cerrado/states_cerrado_biome.shp"
    ).geometries(),
    crs.PlateCarree(),
    facecolor="none",
)

fig, ax = plot.subplots(
    tight=True,
    proj="pcarree",
)

# Formatação do mapa.
ax.format(
    coast=False,
    borders=False,
    innerborders=False,
    labels=True,
    grid=True,
    latlines=3,
    lonlines=3,
    latlim=(-25, -2),
    lonlim=(-61, -41),
    small="8px",
    large="11px",
    title="Risco de Fogo",
)

# Plot da variável. Nome da variável do arquivo: "rf".
map = ax.pcolormesh(
    variavel["lon"],
    variavel["lat"],
    variavel["rf"][0, :, :],
    cmap=cores,
    levels=valores_de_rf,
)

# Adiciona o contorno do bioma.
ax.add_feature(bioma, linewidth=1, edgecolor="k")

#  Adiciona a barra de cores.
x = fig.colorbar(
    map,
    loc="b",
    width="12px",
    shrink=0.87,
    ticklabelsize=6,
    ticks=posicao_categoria,
    ticklabels=categorias_de_rf,
)

# Posicionamento das categorias de risco de fogo na barra de cores.
x.ax.xaxis.set_tick_params(pad=-7)
x.ax.tick_params(size=0)

# Salva a figura no formato ".jpg" com dpi=300.
fig.save("ex03.jpg", transparent=True, dpi=300, bbox_inches="tight", pad_inches=0.02)
