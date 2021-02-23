import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Função que adiciona o label nas barras e a unidade de porcentagem (%).
def define_label (ax, rects, values):
    for rect, value in zip(rects, values):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height, f'{value}', ha='center', va='bottom')


df = pd.read_csv('../../../dados/texto/variaveis_meteorologicas.txt', sep= '\t', names=['Data', 'UR', 'TEMP', 'PREC', 'VelVento', 'DirVento' ])

x = df['PREC']  # Importa os valores de umidade relativa.
classes = ['[0.0-4.5]', '[4.5-8.9]', '[8.9-13.4]', '[13.4-17.8]', '[17.8-22.3]', '[22.3-26.7]']

# Valores do histograma.
valores_histograma = np.histogram(x, bins=6)
print((valores_histograma))

fig, ax = plt.subplots(figsize=(6,3))  # Largua e altura da figura.

ax.hist(x, bins=6, histtype='bar', color='blue', alpha=0.45, rwidth=0.8) 

# Título principal da figura.
plt.title('Histograma de Precipitação', fontsize=10)

# Formatação do eixo x.
plt.xlabel('Classes (mm/dia)', fontsize=8)  # Título do eixo x e o seu tamanho.
ax.set_xlim(0, 27, 3)  # Define o mínimo e o máximo valor do eixo x.
plt.setp(ax.get_xticklabels(), rotation=0, ha="center", rotation_mode="anchor")
plt.xticks([2.3, 6.7, 11.2, 15.6, 20.1, 24.5], classes, fontsize=8)  # Rótulos do eixo x e tamanho.

# Formatação do eixo y.
plt.ylabel('Frequência', fontsize=10)  # Título do eixo y e o seu tamanho.
ax.set_ylim(0, 115)  # Mínimo e máximo valor do eixo y.
ax.set_yticks(ticks=range(0, 130, 20))  # Rótulos do eixo y definido pelo usuário.
plt.yticks(fontsize=8)  # Tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

# Chama a função para adicionar os valores em cada uma das barras.
define_label(ax, ax.containers[0].patches, valores_histograma[0])

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex03.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)