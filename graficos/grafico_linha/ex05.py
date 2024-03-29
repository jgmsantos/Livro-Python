import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Abertura do arquivo temperatura.txt com o separador TAB. Adiciona também o
# título de cada coluna. O arquivo tem formato de 12 linhas por 4 colunas.
# A primeira coluna é o mês, a segunda, a climatologia, a terceira, o ano
# de 2019 e a quarta, o ano de 2020.
df = pd.read_csv(
    "../../dados/texto/temperatura.txt",
    sep="\t",
    names=["Mês", "Climatologia", "2019", "2020"],
)

x = df["Mês"]  # Importa os valores da coluna Mês.
y = df["2020"]  # Importa os valores da coluna 2020.
y_std = np.std(y)  # Cálculo do desvio padrão.

# Largura e altura da figura.
fig, ax = plt.subplots(figsize=(8, 4))

# Gera o plot.
ax.plot(
    x,
    y,
    color="red",
    marker="o",
    linestyle="solid",
    linewidth=2,
    markersize=5,
    label="Temperatura",
)

# Curva com o desvio padrão.
ax.fill_between(x, y - y_std, y + y_std, alpha=0.10, color="red", label="Desvio Padrão")

# Título principal da figura.
plt.title("Temperatura em 2020", fontsize=8)

# Formatação do eixo x.
plt.xlabel("Mês", fontsize=8)
plt.xticks(fontsize=8)
ax.set_xlim(0, 11)

# Formatação do eixo y.
plt.ylabel("Temperatura (ºC)", fontsize=8)
ax.set_ylim(26, 30)
ax.set_yticks(ticks=[26, 26.5, 27, 27.5, 28, 28.5, 29, 29.5, 30])
plt.yticks(fontsize=8)
plt.tick_params(axis="y", right=True)

# Gera a legenda sem borda, define localização e o tamanho da fonte.
plt.legend(frameon=False, loc="upper left", fontsize=8)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig("ex05.jpg", transparent=True, dpi=300, bbox_inches="tight", pad_inches=0)
