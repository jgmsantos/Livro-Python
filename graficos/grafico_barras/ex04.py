import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Função que adiciona o label nas barras e a unidade de porcentagem (%).
def define_label(ax, rects, values):
    for rect, value in zip(rects, values):
        height = rect.get_height()
        ax.text(
            rect.get_x() + rect.get_width() / 2,
            height,
            f"{value}%",
            ha="center",
            va="bottom",
            fontsize=8,
        )


# Abertura do arquivo utilizando o separador espaço e
# adiciona o título como primeira linha.
df = pd.read_csv("../../dados/texto/spi.classes.txt", sep=" ", names=["2019", "2020"])

df = df.astype(int)  # Define o conjunto de dados como valor inteiro.

total_classes = 3  # Total de classes avaliadas.
classes = ["Eventos Úmidos", "Eventos Normais", "Eventos Secos"]
ANO_ANTERIOR = "2019"
ANO_ATUAL = "2020"
ano2019 = df[ANO_ANTERIOR].values  # Valores percentuais.
ano2020 = df[ANO_ATUAL].values  # Valores percentuais.
largura_barra = 0.25  # Largura da barra.

r1 = np.arange(len(classes))  # Vetor com os índices.
x1 = [y - 0.13 for y in r1]
x2 = [y + 0.13 for y in r1]

fig, ax = plt.subplots()

# Plota o gráfico da primeira barra.
ax.bar(x1, ano2019, width=largura_barra, color="blue", label=ANO_ANTERIOR)
# Plota o gráfico da segunda barra.
ax.bar(x2, ano2020, width=largura_barra, color="green", label=ANO_ATUAL)

# Chama a função para adicionar os rótulos em cada uma das barras.
define_label(ax, ax.containers[0].patches, ano2019)
define_label(ax, ax.containers[1].patches, ano2020)

# Formatação do eixo x.
plt.xticks(np.arange(total_classes), classes, fontsize=8)

# Formatação do eixo y.
plt.ylim(0, 100)  # Define o mínimo e máximo valor do eixo y.
plt.yticks(fontsize=8)  # Tamanho dos rótulos do eixo y.
# Desabilita os rótulos de ambos os eixos esquerdo e direito.
plt.tick_params(axis="y", which="both", left=False, right=False, labelleft=False)

# Gera a legenda:
plt.legend(frameon=False)  # Desabilita a borda da legenda.

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig("ex04.jpg", transparent=True, dpi=300, bbox_inches="tight", pad_inches=0)
