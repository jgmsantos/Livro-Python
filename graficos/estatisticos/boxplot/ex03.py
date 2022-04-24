import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(
    "../../../dados/texto/variaveis_meteorologicas.txt",
    sep="\t",
    names=[
        "Data",
        "Umidade Relativa",
        "Temperatura",
        "Precipitacao",
        "VelVento",
        "DirVento",
    ],
)

UR = df["Umidade Relativa"]  # Importa os valores de umidade relativa.
TEMP = df["Temperatura"]  # Importa os valores de temperatura.

# Gera o plot.
plt.boxplot(
    [UR, TEMP],
    showfliers=True,
    notch=False,
    patch_artist=True,
    showmeans=True,
    meanline=True,
)

box = plt.boxplot([UR, TEMP], patch_artist=True)

colors = ["powderblue", "tan"]  # Define cores para cada caixa.

for patch, color in zip(box["boxes"], colors):
    patch.set_facecolor(color)

# Título principal da figura.
plt.title("Boxplot de Umidade Relativa e Temperatura", fontsize=8)

# Formatação do eixo x.
plt.xticks(ticks=[1, 2], labels=["Umidade\nRelativa", "Temperatura"], fontsize=8)

# Formatação do eixo y.
plt.ylabel("Umidade Relativa (%) e Temperatura (ºC)", fontsize=8)
plt.ylim(0, 100)
plt.yticks(ticks=range(0, 110, 10), fontsize=8)
plt.tick_params(axis="y", right=True)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig("ex03.jpg", transparent=True, dpi=300, bbox_inches="tight", pad_inches=0)
