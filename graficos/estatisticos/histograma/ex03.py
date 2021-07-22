import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../../../dados/texto/variaveis_meteorologicas.txt', sep= '\t', names=['Data', 'UR', 'TEMP', 'Prec','VelVento', 'DirVento' ])

x = df['VelVento']  # Importa os valores de velocidade do vento.
classes = ['[0-2]', '[2-4]', '[4-6]', '[6-8]', '[8-10]', '[>10]']

fig, ax = plt.subplots(figsize=(6,3))  # Largura e altura da figura.

# Gera o plot.
ax.hist(x, bins=[0, 2, 4, 6, 8, 10], histtype='bar', color='yellow', alpha=0.45, rwidth=0.8) 

# Título principal da figura.
plt.title('Histograma de Velocidade do Vento: 2003-2020', fontsize=8)

# Formatação do eixo x.
plt.xlabel('Classes (km/h)', fontsize=8)  # Título do eixo x e o tamanho da fonte.
ax.set_xlim(0, 12)  # Define o mínimo e o máximo valor do eixo x.
plt.setp(ax.get_xticklabels(), rotation=0, ha="center", rotation_mode="anchor")
plt.xticks([1, 3, 5, 7, 9, 11], classes, fontsize=8)  # Rótulos do eixo x e tamanho.

# Formatação do eixo y.
plt.ylabel('Frequência', fontsize=8)  # Título do eixo y e o tamanho da fonte.
ax.set_ylim(0, 140)  # Mínimo e máximo valor do eixo y.
ax.set_yticks(ticks=range(0, 145, 20))  # Rótulos do eixo y definido pelo usuário.
plt.yticks(fontsize=8)  # Tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex03.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)