import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Função que adiciona o label nas barras e a unidade de porcentagem (%).
def define_label (ax, rects, values):
    for rect, value in zip(rects, values):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height, f'{value}', ha='center', va='bottom')


df = pd.read_csv('../../../dados/texto/variaveis_meteorologicas.txt', sep= '\t', names=['Data', 'UR', 'TEMP', 'PREC', 'VelVento', 'DirVento' ])

x = df['TEMP']  # Importa os valores de umidade relativa.
classes = ['[13.1-16.6]', '[16.6-20.1]', '[20.1-23.6]', '[23.6-27.1]', '[27.1-30.6]', '[30.4-34.1]']

# Valores do histograma.
valores_histograma = np.histogram(x, bins=6)
print((valores_histograma))

fig, ax = plt.subplots(figsize=(6,3))  # Largua e altura da figura.

ax.hist(x, bins=6, histtype='bar', color='red', alpha=0.45, rwidth=0.8) 

# Título principal da figura.
plt.title('Histograma de Temperatura', fontsize=10)

# Formatação do eixo x.
plt.xlabel('Classes (ºC)', fontsize=8)  # Título do eixo x e o seu tamanho.
ax.set_xlim(13, 34, 2)  # Define o mínimo e o máximo valor do eixo x.
plt.setp(ax.get_xticklabels(), rotation=0, ha="center", rotation_mode="anchor")
plt.xticks([14.9, 18.4, 21.9, 25.4, 28.9, 32.3], classes, fontsize=8)  # Rótulos do eixo x e tamanho.

# Formatação do eixo y.
plt.ylabel('Frequência', fontsize=10)  # Título do eixo y e o seu tamanho.
ax.set_ylim(0, 50)  # Mínimo e máximo valor do eixo y.
ax.set_yticks(ticks=range(0, 55, 10))  # Rótulos do eixo y definido pelo usuário.
plt.yticks(fontsize=8)  # Tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

# Chama a função para adicionar os valores em cada uma das barras.
define_label(ax, ax.containers[0].patches, valores_histograma[0])

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex02.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)