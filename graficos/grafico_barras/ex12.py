import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Abertura do arquivo utilizando o separador TAB e adiciona o título como primeira linha.
df = pd.read_csv('../../dados/texto/variaveis_meteorologicas.txt', sep= '\t', names=['Data','UR','Temp','PREC','VelVento','DirVento'])

x = np.arange(216)  # Desde 01/2020 12/2020 = 216 meses.
meses = ['Jan2003', 'Jan2004', 'Jan2005', 'Jan2006', 'Jan2007', 'Jan2008', 'Jan2009', 'Jan2010', 'Jan2011', 'Jan2012', 'Jan2013', 'Jan2014', 'Jan2015', 'Jan2016', 'Jan2017', 'Jan2018', 'Jan2019', 'Jan2020']

ur = df['UR']
temp = df['Temp']

fig, ax = plt.subplots(figsize=(6,3))  # Largua e altura da figura.

# Plot do gráfico de barra.
ax.bar(x, ur, 0.75, color="green", alpha=0.5, label='Umidade Relativa')

ax2 = ax.twinx()

# Plot do gráfico de linha.
ax2.plot(x, temp, color="chocolate", alpha=0.8, label='Temperatura')

# Título da figura.
plt.title('Umidade Relativa e Temperatura - 2003 a 2020', fontsize=8)

#  Formatação do eixo x.
ax.set_xlim(-1, 216, 1)  # Define o mínimo e o máximo valor do eixo x.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
plt.xticks(np.arange(0,215,12), meses, fontsize=8)  # Rótulos do eixo x, tamanho e orientação.

#  Formatação do eixo y esquerdo.
ax.set_ylabel('Umidade Relativa (%)', fontsize=8)  # Tamanho do título do eixo y.
ax.set_ylim(0, 100)  # Define o mínimo e máximo valor do eixo y.
ax.set_yticks(np.arange(0, 105, step=10))  # Define o mínimo e máximo valor do eixo y.
ax.tick_params(labelsize=8)  # Tamanho dos seus rótulos do eixo y esquerdo.

#  Formatação do eixo y direito.
ax2.set_ylabel('Temperatura (ºC)', fontsize=8)  # Tamanho do título do eixo y.
ax2.set_ylim(15, 25)  # Define o mínimo e máximo valor do eixo y.
ax2.set_yticks(np.arange(15, 26, step=1))  # Define o mínimo e máximo valor do eixo y, tamanho dos seus rótulos.
ax2.tick_params(labelsize=8)  # Tamanho dos seus rótulos do eixo y direito.

# Gera a legenda sem borda, define localização e o seu tamanho.
ax.legend(frameon =False, loc='upper left', fontsize=8, bbox_to_anchor=(0.4, 0.96))
ax2.legend(frameon =False, loc='upper left', fontsize=8, bbox_to_anchor=(0.4, 1.02))

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex12.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)  