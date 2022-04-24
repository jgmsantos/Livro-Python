import matplotlib.pyplot as plt
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
y = df["Climatologia"]  # Importa os valores da coluna Climatologia.

# Largura e altura da figura.
fig, ax = plt.subplots(figsize=(8, 4))

# Gera o plot.
ax.plot(
    x,
    y,
    color="green",
    marker="o",
    linestyle="solid",
    linewidth=2,
    markersize=5,
    label="Temperatura",
)

# Título principal da figura.
plt.title("Climatologia de Temperatura", fontsize=8)

# Formatação do eixo x.
plt.xlabel("Meses", fontsize=8)
plt.xticks(fontsize=8)

# Formatação do eixo y.
plt.ylabel("Temperatura (ºC)", fontsize=8)
ax.set_ylim(25, 28)
ax.set_yticks(ticks=[25, 25.5, 26, 26.5, 27, 27.5, 28])
plt.yticks(fontsize=8)
plt.tick_params(axis="y", right=True)

# Gera a legenda sem borda, define a localização e o tamanho da fonte.
plt.legend(frameon=False, loc="upper left", fontsize=8)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig("ex01.jpg", transparent=True, dpi=300, bbox_inches="tight", pad_inches=0)
