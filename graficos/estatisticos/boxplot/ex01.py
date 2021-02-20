import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('../../../dados/texto/umidade_relativa_temperatura.txt', sep= '\t', names=['Data', 'Umidade Relativa', 'Temperatura'])

UR = df['Umidade Relativa']  # Importa os valores de umidade relativa.

plt.boxplot(UR, showfliers=True, notch= False, patch_artist=True)

# Título principal da figura.
plt.title('Boxplot de Umidade Relativa', fontsize=12)

# Formatação do eixo x.
plt.xticks(ticks=None, labels=None)  # Rótulos do eixo y definido pelo usuário.
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)  # Desabilita os rótulos de ambos os eixos esquerdo e direito.

# Formatação do eixo y.
plt.ylabel('Umidade Relativa (%)', fontsize=10)  # Título do eixo y e o seu tamanho.
plt.ylim(0, 100)  # Mínimo e máximo valor do eixo y.
plt.yticks(ticks=range(0, 110, 10), fontsize=10)  # Rótulos do eixo y definido pelo usuário.
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex01.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)