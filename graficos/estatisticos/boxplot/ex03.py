import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('../../../dados/texto/variaveis_meteorologicas.txt', sep= '\t', names=['Data', 'Umidade Relativa', 'Temperatura', 'Precipitacao', 'VelVento', 'DirVento'])

UR = df['Umidade Relativa']  # Importa os valores de umidade relativa.
TEMP = df['Temperatura']  # Importa os valores de temperatura.

plt.boxplot([UR, TEMP], showfliers=True, notch= False, patch_artist=True, showmeans=True, meanline=True)

box = plt.boxplot([UR, TEMP], patch_artist=True)

colors = ['powderblue', 'tan']
 
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Título principal da figura.
plt.title('Boxplot de Umidade Relativa e Temperatura', fontsize=12)

# Formatação do eixo x.
plt.xticks(ticks=[1, 2], labels=['Umidade\nRelativa', 'Temperatura'])  # Rótulos do eixo y definido pelo usuário.

# Formatação do eixo y.
plt.ylim(0, 100)  # Mínimo e máximo valor do eixo y.
plt.yticks(ticks=range(0, 110, 10), fontsize=10)  # Rótulos do eixo y definido pelo usuário.
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex03.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)