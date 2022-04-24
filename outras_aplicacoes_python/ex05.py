from py3grads import Grads
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates

"""
Nota: O py3grads funciona apenas se haver uma instalação prévia do grads (ou opengrads) no sistema operacional em uso,
de modo que o comando 'grads' seja reconhecido em seu terminal. Este método foi testado em ambiente Ubuntu, mas deve
funcionar também em WSL no Windows, ou até no próprio Windows via PowerShell + OpenGrADS.
"""
## Carregando ambiente GrADS
ga = Grads(verbose=False)

##  Lendo arquivo descritor
ga("open wrf2022021700/WRF_cpt_05KM_2022021700.ctl")

## Série temporal em pontos específicos (no ponto de grade mais próximo do WRF)
lats = [-22.5306, -15.7894, -13.0166, -22.6888, -19.9799]
lons = [-43.1695, -47.9258, -38.5166, -45.0055, -43.9586]
locs = [
    "Petropolis - RJ",
    "Brasilia - DF",
    "Salvador - BA",
    "Cachoeira Paulista - SP",
    "Belo Horizonte - MG",
]

## Consultando período de previsão no descritor
ga("set t 1 last")
time = ga("q time")

## Criando dataframe com informações de tempo consultadas
inicio = pd.to_datetime(list(time[0])[0].split()[2], format="%HZ%d%b%Y")
final = pd.to_datetime(list(time[0])[0].split()[4], format="%HZ%d%b%Y")
df = pd.DataFrame(index=pd.date_range(start=inicio, end=final, freq="H"), columns=locs)

## Obtendo série temporal para cada localidade e guardando no dataframe
dat = []
for idx, _ in enumerate(lats):
    ga(f"set lat {lats[idx]}")
    ga(f"set lon {360 + lons[idx]}")
    apcp = ga.exp("APCPsfc")
    print(lats[idx], lons[idx], locs[idx], apcp)
    df[locs[idx]] = apcp

#%%
## Limpando quaisquer outras figuras anteriores e criando uma nova
plt.close("all")
fig, ax = plt.subplots(figsize=(12, 5))

xtime = (
    df.index.to_pydatetime()
)  ## Variável criada para converter DatetimeIndex do Pandas para formato numérico interpretado pelo matplotlib.

## Plotando a série temporal de cada localidade
for _, p in enumerate(locs):
    ax.plot(xtime, df[p], label=p, lw=2)

## Personalizando o eixo x de hora/data
ax.set_xlim(xtime[0], xtime[-1])
ax.xaxis.set_major_formatter(mdates.DateFormatter("%H UTC\n%d%b"))
ax.xaxis.set_major_locator(mdates.HourLocator(interval=12))
ax.xaxis.set_minor_formatter(mdates.DateFormatter(""))
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=1))

## Outras personalizações: grade, títulos e legenda
ax.grid(which="major", linestyle="--", color="gray", alpha=0.5)
ax.set_title("WRF 5km CPTEC/INPE", loc="left")
ax.set_title(
    f"Previsão de 84h (Inicio: { inicio.strftime('%HUTC %d%b%Y') })", loc="right"
)
ax.set_ylabel("Precipitação acumulada (mm)")
ax.legend()

## Salvando a figura de modo ajustado (resolução, bordas, etc)
fig.savefig("pygrads_time_series.png", dpi=300, bbox_inches="tight", pad_inches=0.03)
