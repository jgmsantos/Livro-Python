import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#### Funções:
# Função que adiciona o label nas barras e a unidade de porcentagem (%).
def define_label (ax, rects, values):
    for rect, value in zip(rects, values):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height, f'{value}', ha='center', va='bottom')


# Abertura do arquivo utilizando o separador espaço e adicionando título como primeira linha.
df = pd.read_csv('../../dados/texto/media_mensal.txt', sep= '\t', names=['Mês','NDSC', 'UR', 'TEMP', 'PREC'])

total_meses = 4 # Total de meses a serem utilizados.
meses = df['Mês']  # Nome dos rótulos que vão aparecer no eixo x.
ndsc = df['NDSC']  # Valores percentuais.
largura_barra = 0.25  # Largura da barra.

fig, ax = plt.subplots(figsize=(7, 3))

# Plota o gráfico da primeira barra.
ax.bar(meses, ndsc, width=largura_barra, color='#81d4fa', label=meses)

# Chama a função para adicionar os valores em cada uma das barras.
define_label(ax, ax.containers[0].patches, ndsc)

# Formatação do eixo y.
plt.ylim(0, 35)  # Define o mínimo e máximo valor do eixo y.
plt.ylabel('Total de dias', fontsize=10)  # Tamanho do título do eixo y.
plt.yticks(fontsize=10)  # Tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

# Formatação do eixo x.
plt.xticks(meses, fontsize=10)  # Rótulos do eixo x e tamanho.
plt.xlabel('Mês', fontsize=10)  # Tamanho do título do eixo x.

# Título da figura.
plt.title('Número de Dias Sem Chuva')

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex10.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)