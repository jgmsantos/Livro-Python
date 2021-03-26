import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('../../../dados/texto/variaveis_meteorologicas.txt', sep= '\t', names=['Data', 'UR', 'TEMP', 'Prec','VelVento', 'DirVento' ])

x = df['TEMP']  # Importa os valores de temperatura.
classes = ['[10-15]', '[15-20]', '[20-25]', '[25-30]', '[30-35]', '[>35]']

fig, ax = plt.subplots(figsize=(6,3))  # Largura e altura da figura.

# Gera o plot.
ax.hist(x, bins=[10, 15, 20, 25, 30, 35], histtype='bar', color='red', alpha=0.45, rwidth=0.8) 

# Título principal da figura.
plt.title('Histograma de Temperatura: 2003-2020', fontsize=8)

# Formatação do eixo x.
plt.xlabel('Classes (ºC)', fontsize=8)  # Título do eixo x e o tamanho da fonte.
ax.set_xlim(10, 40)  # Define o mínimo e o máximo valor do eixo x.
plt.setp(ax.get_xticklabels(), rotation=0, ha="center", rotation_mode="anchor")
plt.xticks([12.5, 17.5, 22.5, 27.5, 32.5, 37.5], classes, fontsize=8)  # Rótulos do eixo x e tamanho.

# Formatação do eixo y.
plt.ylabel('Frequência', fontsize=8)  # Título do eixo y e o tamanho da fonte.
ax.set_ylim(0, 140)  # Mínimo e máximo valor do eixo y.
ax.set_yticks(ticks=range(0, 145, 20))  # Rótulos do eixo y definido pelo usuário.
plt.yticks(fontsize=8)  # Tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex01.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)