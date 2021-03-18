import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Abertura do arquivo utilizando o separador espaço e adiciona o título como primeira linha.
df1 = pd.read_csv('../../dados/texto/ERA5.Climatologia.txt', sep='\t', names=['Mês','UR', 'TEMP', 'VEL', 'DIR'])
df2 = pd.read_csv('../../dados/texto/precipitacao.txt', sep='\t', names=['Mês', 'Clima', '2019', '2020'])

meses = df1['Mês']  # Nome dos rótulos que vão aparecer no eixo x.
ur = df1['UR']
temp = df1['TEMP']
prec = df2['Clima']

fig, ax = plt.subplots(figsize=(6,3))  # Largura e altura da figura.

# Plot do gráfico de barra.
ax.bar(meses, prec, 0.35, color="blue", alpha=0.5, label='Precipitação')

# Plota do eixo esquerdo gráfico de linha (Umidade Relativa).
ax.plot(meses, ur, color="green", marker='o', linestyle='solid', linewidth=2, markersize=5, alpha=0.5, label='Umidade Relativa')

ax2 = ax.twinx()

# Plota do eixo direito do gráfico de linha (Umidade Temperatura).
ax2.plot(meses, temp, color="red", marker='o', linestyle='solid', linewidth=2, markersize=5,alpha=0.5, label='Temperatura')

# Título da figura.
plt.title('Média Mensal - 2003 a 2020', fontsize=8)

#  Formatação do eixo x.
plt.xticks(meses, fontsize=8)  # Rótulos do eixo x e tamanho.
plt.xlabel('Mês', fontsize=8)  # Tamanho do título do eixo x.

# Formatação do eixo y esquerdo.
ax.set_ylabel('Precipitação (mm/mês), Umidade Relativa (%)', fontsize=8)  # Tamanho do título do eixo y.
ax.set_ylim(0, 300)  # Define o mínimo e máximo valor do eixo y.
ax.set_yticks(np.arange(0, 310, step=25))  # Define o mínimo e máximo valor do eixo y.
ax.tick_params(labelsize=7)  # Tamanho dos seus rótulos do eixo y esquerdo.

# Formatação do eixo y direito.
ax2.set_ylabel('Temperatura (ºC)', fontsize=8)  # Tamanho do título do eixo y.
ax2.set_ylim(0, 30)  # Define o mínimo e máximo valor do eixo y.
ax2.set_yticks(np.arange(0, 35, step=5))  # Define o mínimo e máximo valor do eixo y, tamanho dos seus rótulos.
ax2.tick_params(labelsize=8)  # Tamanho dos seus rótulos do eixo y direito.

# Gera a legenda sem borda, define localização e o seu tamanho.
ax.legend(frameon =False, loc='upper left', fontsize=8, bbox_to_anchor=(0.4, 0.92))
ax2.legend(frameon =False, loc='upper left', fontsize=8, bbox_to_anchor=(0.4, 0.98))

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex14.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)