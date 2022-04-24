import matplotlib.pyplot as plt
import pandas as pd
import metpy.calc as mpcalc
from metpy.plots import SkewT
from metpy.units import units
from datetime import datetime
from siphon.simplewebservice.wyoming import WyomingUpperAir


"""
Abaixo, a solicitação da radiossonda é baseada no código ICAO do aeroporto. A lista completa de códigos ICAO dos aeroportos brasileiros está disponível no link: https://pt.wikipedia.org/wiki/Lista_de_aeroportos_do_Brasil_por_c%C3%B3digo_aeroportu%C3%A1rio_ICAO
Importante reforçar que nem todo aeroporto brasileiro faz lançamento de radiossondas.
"""


# Solicitando os dados e convertendo-os em DataFrame.
date = datetime(2021, 10, 14, 12)
station = "SBBR"
df = WyomingUpperAir.request_data(date, station)

p = df["pressure"].values * units(df.units["pressure"])
T = df["temperature"].values * units(df.units["temperature"])
Td = df["dewpoint"].values * units(df.units["dewpoint"])
u = df["u_wind"].values * units(df.units["u_wind"])
v = df["v_wind"].values * units(df.units["v_wind"])

"""# Fazendo o processamento dos dados com MetPy"""
# Fazendo o plot Skew-T Log-P, tradicional na meteorologia.
fig = plt.figure(figsize=(9, 9))
skew = SkewT(fig, rotation=45)
skew.plot(p, T, "r")
skew.plot(p, Td, "g")
skew.plot_barbs(p, u, v)

# Calculando parâmetros termodinâmicos do ponto de ascenção da parcela de ar.
lcl_pressure, lcl_temperature = mpcalc.lcl(p[0], T[0], Td[0])
skew.plot(lcl_pressure, lcl_temperature, "ko", markerfacecolor="black")

# Calculando o perfil vertical de ascenção da parcela de ar.
prof = mpcalc.parcel_profile(p, T[0], Td[0]).to("degC")
skew.plot(p, prof, "k", linewidth=2)

# Plot das área de CAPE e CIN.
skew.shade_cin(p, T, prof, Td)
skew.shade_cape(p, T, prof)

# Adicionando as linhas de perfil adiabático (úmida e seca) e linhas da razão de mistura.
skew.plot_dry_adiabats()
skew.plot_moist_adiabats()
skew.plot_mixing_lines()

# Ajustes finais da figura.
skew.ax.set_ylim(1000, 100)
plt.title(
    f"Estação: {df['station'][0]} (n={df['station_number'][0]}) | Data: {df['time'][0]}"
)
plt.ylabel("Pressão atmosférica (hPa)")
plt.xlabel("Temperatura (°C)")

# Salvando a figura.
fig.savefig("ex03.png", dpi=300, bbox_inches="tight", pad_inches=0.01)
