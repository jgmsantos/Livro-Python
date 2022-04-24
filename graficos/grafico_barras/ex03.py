import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Abertura do arquivo temperatura.txt com o separador TAB. Adiciona
# também o título de cada coluna. A primeira coluna é o mês, a segunda,
# a climatologia, a terceira, o ano de 2019 e a quarta, o ano de 2020.
df = pd.read_csv(
    "../../dados/texto/temperatura.txt",
    sep="\t",
    names=["Mês", "Climatologia", "2019", "2020"],
)

x = df["Mês"]  # Importa os valores da coluna Mês.
y1 = df["Climatologia"]  # Importa os valores da coluna Climatologia.
y2 = df["2020"]  # Importa os valores da coluna 2020.

# Anomalia = desvio em relação ao valor médio (climatologia).
anomalia = y2 - y1

# Separa os valores positivos e negativos.
acima_limiar = np.maximum(anomalia - 0, 0)
abaixo_limiar = np.minimum(anomalia, 0)

fig, ax = plt.subplots(figsize=(6, 3))  # Largura e altura da figura.

# Gera o plot com base nos limiares e separa o que é
# positivo (negativo) com vermelho (azul).
ax.bar(x, acima_limiar, 0.75, color="red", alpha=0.5)
ax.bar(x, abaixo_limiar, 0.75, color="blue", alpha=0.5)

# Título principal da figura.
plt.title("Anomalia de Temperatura", fontsize=8)

# Formatação do eixo x.
plt.xlabel("Mês", fontsize=8)
plt.xticks(fontsize=8)  # Tamanho dos rótulos do eixo x.
plt.xlim(-0.5, 11.5)  # Define o mínimo e o máximo valor do eixo x.

# Formatação do eixo y.
plt.ylabel("Temperatura (ºC)", fontsize=8)
ax.set_ylim(-0.5, 1.5)  # Mínimo e máximo valor do eixo y.
# Rótulos do eixo y definido pelo usuário.
ax.set_yticks(ticks=(np.arange(-0.5, 2, 0.5)))
plt.yticks(fontsize=8)  # Tamanho dos rótulos do eixo y.
plt.tick_params(axis="y", right=True)  # Habilita o tickmark do eixo direito.

# Linha no valor zero, espessura = 0.5 e cor = black.
plt.axhline(linestyle="-", y=0, linewidth=0.5, color="black")

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig("ex03.jpg", transparent=True, dpi=300, bbox_inches="tight", pad_inches=0)
