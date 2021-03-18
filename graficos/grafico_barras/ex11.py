import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Abertura do arquivo utilizando o separador TAB e adiciona o título como primeira linha.
df = pd.read_csv('../../dados/texto/variaveis_meteorologicas.txt', sep= '\t', names=['Data','UR','Temp','PREC','VelVento','DirVento'])

x = np.arange(216)  # Desde 01/2020 12/2020 = 216 meses.
meses = ['Jan2003', 'Jan2004', 'Jan2005', 'Jan2006', 'Jan2007', 'Jan2008', 'Jan2009', 'Jan2010', 'Jan2011', 'Jan2012', 'Jan2013', 'Jan2014', 'Jan2015', 'Jan2016', 'Jan2017', 'Jan2018', 'Jan2019', 'Jan2020']

y = df['PREC']

fig, ax = plt.subplots(figsize=(6,3))  # Largura e altura da figura.

ax.bar(x, y, 0.75, color="blue", alpha=0.5)

# Título da figura.
plt.title('Precipitação mensal - 2003 a 2020', fontsize=8)

#  Formatação do eixo x.
plt.xlim(-1, 216, 1)  # Define o mínimo e o máximo valor do eixo x.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
plt.xticks(np.arange(0,215,12), meses, fontsize=8)  # Rótulos do eixo x, tamanho e orientação.

#  Formatação do eixo y.
plt.ylabel('Precipitação (mm/mês)', fontsize=8)  # Tamanho do título do eixo y.
plt.ylim(0, 500)  # Define o mínimo e máximo valor do eixo y.
plt.yticks(np.arange(0, 505, step=50), fontsize=8)  # Define o mínimo e máximo valor do eixo y, tamanho dos seus rótulos.
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex11.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)  