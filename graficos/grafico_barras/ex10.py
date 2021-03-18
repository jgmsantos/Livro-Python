import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Função que adiciona o label nas barras e a unidade.
def define_label (ax, rects, values):
    for rect, value in zip(rects, values):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height, f'{value}', ha='center', va='bottom')


# Abertura do arquivo utilizando o separador espaço e adiciona o título como primeira linha.
df = pd.read_csv('../../dados/texto/media_mensal.txt', sep= '\t', names=['Mês','NDSC', 'UR', 'TEMP', 'PREC'])

meses = df['Mês']  # Nome dos rótulos que vão aparecer no eixo x.
ndsc = df['NDSC']  # Valores percentuais.

fig, ax = plt.subplots(figsize=(7, 3))  # Largura e altura da figura.

# Plota o gráfico.
ax.bar(meses, ndsc, width=0.25, color='#81d4fa', label=meses)

# Chama a função para adicionar os valores em cada uma das barras.
define_label(ax, ax.containers[0].patches, ndsc)

# Título da figura.
plt.title('Número de Dias Sem Chuva', fontsize=8)

# Formatação do eixo x.
plt.xticks(meses, fontsize=8)  # Rótulos do eixo x e tamanho.
plt.xlabel('Mês', fontsize=8)  # Tamanho do título do eixo x.

# Formatação do eixo y.
plt.ylim(0, 35)  # Define o mínimo e máximo valor do eixo y.
plt.ylabel('Total de dias', fontsize=8)  # Tamanho do título do eixo y.
plt.yticks(fontsize=8)  # Tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex10.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)