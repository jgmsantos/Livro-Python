import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('../../../dados/texto/variaveis_meteorologicas.txt', sep= '\t', names=['Data', 'UR', 'TEMP', 'Prec','VelVento', 'DirVento' ])

x = df['Prec']  # Importa os valores.
classes = ['[0-10]', '[10-20]', '[20-30]', '[30-40]', '[40-50]', '[>50]']

fig, ax = plt.subplots(figsize=(6,3))  # Largua e altura da figura.

ax.hist(x, bins=[0, 10, 20, 30, 40, 50], histtype='bar', color='blue', alpha=0.45, rwidth=0.8) 

# Título principal da figura.
plt.title('Histograma de Precipitação: 2003-2020', fontsize=10)

# Formatação do eixo x.
plt.xlabel('Classes (mm/mês)', fontsize=8)  # Título do eixo x e o seu tamanho.
ax.set_xlim(0, 60)  # Define o mínimo e o máximo valor do eixo x.
plt.setp(ax.get_xticklabels(), rotation=0, ha="center", rotation_mode="anchor")
plt.xticks([5, 15, 25, 35, 45, 55], classes, fontsize=8)  # Rótulos do eixo x e tamanho.

# Formatação do eixo y.
plt.ylabel('Frequência', fontsize=10)  # Título do eixo y e o seu tamanho.
ax.set_ylim(0, 140)  # Mínimo e máximo valor do eixo y.
ax.set_yticks(ticks=range(0, 145, 20))  # Rótulos do eixo y definido pelo usuário.
plt.yticks(fontsize=8)  # Tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

#   Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex04.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)