import xarray as xr
import proplot as plot
import numpy as np


## Ignora mensagem de aviso pois no cálculo da correlação
# são encontrados valores UNDEF.
np.seterr(divide="ignore", invalid="ignore")

# Define o tamanho da fonte do título, rótulos e títulos dos eixos x e y.
plot.rc.fontsize = 10

# Abertura do arquivo.
tsm = xr.open_dataset("../../../dados/netcdf/sst.1981.2010.nc")

# Cálculo da anomalia (valor observado - média).
atsm = tsm.groupby("time.month") - tsm.groupby("time.month").mean("time")

# Anomalia de SST na região do Niño 3.4
nino34 = atsm.sel(lon=slice(190, 240), lat=slice(5, -5)).mean(("lon", "lat"))

fig, ax = plot.subplots(figsize=(8, 4))

# Plota da série temporal da SST na região do Niño 3.4.
ax.bar(np.array(nino34["time"]), np.array(nino34["sst"]), negpos=True)

ax.format(
    ylabel="Anomalia de SST ($\degree$C)",
    title="Anomalia de SST na região do Niño 3.4",
    ylim=(-3, 3),
    yminorlocator=0.5,
    ylocator=np.arange(-3, 3.5, 0.5),
    yformatter="{x:.1f}",
    xlim=(np.datetime64("1981-01-01"), np.datetime64("2010-12-01")),
    xlocator="year",
    xminorlocator="year",
    xformatter="%b%Y",
)

ax.tick_params(axis="y", right=True)  # Habilita o tickmark do eixo direito.

# Adiciona uma linha no valor 0.5°C no eixo y que define o evento El Niño.
ax.axhline(0.5, color="red", linestyle="--")

# Adiciona linha no valor -0.5C no eixo y que define o evento La Niña.
ax.axhline(-0.5, color="blue", linestyle="--")

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
fig.savefig("ex01.jpg", transparent=True, dpi=300, bbox_inches="tight", pad_inches=0)
