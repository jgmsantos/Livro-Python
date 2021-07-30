import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Função que adiciona o label nas barras para valores númericos.
def define_label (ax, rects, values):
    for rect, value in zip(rects, values):
        if value !=0:
             height = rect.get_height()
             ax.text(rect.get_x() + rect.get_width() / 2, 
             height, f'{value:.0f}%', 
             ha='center', 
             va='bottom', 
             fontsize=8)


df = pd.read_csv('../../../dados/texto/variaveis_meteorologicas.txt', 
                 sep= '\t', 
                 names=['Data', 'UR', 'TEMP', 'Prec','VelVento', 'DirVento' ])

x = df['TEMP']  # Importa os valores de temperatura.
classes = ['[10-15]', '[15-20]', '[20-25]', '[25-30]', '[30-35]', '[>35]']

fig, ax = plt.subplots(figsize=(6,3))  # Largura e altura da figura.

# Gera o plot.
y = ax.hist(x, bins=[10, 15, 20, 25, 30, 35], 
            histtype='bar', 
            color='red', 
            alpha=0.45, 
            rwidth=0.8) 

# Calcula a porcentagem.
soma_temp = sum(list(y[0]))
pct_temp = (list(y[0])/soma_temp)*100

# Título principal da figura.
plt.title('Histograma de Temperatura: 2003-2020', fontsize=8)

# Formatação do eixo x.
plt.xlabel('Classes (ºC)', fontsize=8)  # Título e tamanho do eixo.
ax.set_xlim(10, 40)  # Define o mínimo e o máximo valor do eixo x.
plt.setp(ax.get_xticklabels(), rotation=0, ha="center", rotation_mode="anchor")
  # Rótulos do eixo x e tamanho.
plt.xticks([12.5, 17.5, 22.5, 27.5, 32.5, 37.5], classes, fontsize=8)

# Formatação do eixo y.
plt.ylabel('Frequência', fontsize=8)  # Título do eixo y e o tamanho da fonte.
ax.set_ylim(0, 160)  # Mínimo e máximo valor do eixo y.
ax.set_yticks(ticks=range(0, 165, 20))  # Rótulos do eixo y.
plt.yticks(fontsize=8)  # Tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

# Função que adiciona os rótulos em cada barra.
define_label(ax, ax.containers[0].patches, pct_temp)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex01.jpg', transparent=True, dpi=300, bbox_inches='tight', 
             pad_inches=0)