import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Abertura do arquivo utilizando o separador espaço e adicionando título como primeira linha.
df = pd.read_csv('../../dados/texto/media_mensal.txt', sep= '\t', names=['Mês','NDSC', 'UR', 'TEMP', 'PREC'])

meses = df['Mês']  # Nome dos rótulos que vão aparecer no eixo x.
ur = df['UR']
temp = df['TEMP']
prec = df['PREC']

# Gera o plot com base nos limiares e separa o que é positivo (negativo) com vermelho (azul).
fig, ax = plt.subplots(figsize=(6,3))  # Largua e altura da figura.

# Plot do gráfico de barra.
ax.bar(meses, prec, 0.35, color="gray", alpha=0.5, label='Precipitação')
ax.plot(meses, ur, color="blue", marker='o', linestyle='solid', linewidth=2, markersize=5, alpha=0.5, label='Umidade Relativa')

ax2 = ax.twinx()

# Plot do gráfico de linha.
ax2.plot(meses, temp, color="red", marker='o', linestyle='solid', linewidth=2, markersize=5,alpha=0.5, label='Temperatura')

# Título da figura.
plt.title('Serra do Cipó', fontsize=10)

#  Formatação do eixo y esquerdo.
ax.set_ylabel('Precipitação (mm/dia), Umidade Relativa (%)', fontsize=7)  # Tamanho do título do eixo y.
ax.set_ylim(0, 140)  # Define o mínimo e máximo valor do eixo y.
ax.set_yticks(np.arange(0, 145, step=20))  # Define o mínimo e máximo valor do eixo y.
ax.tick_params(labelsize=7)  # Tamanho dos seus rótulos do eixo y esquerdo.

#  Formatação do eixo y direito.
ax2.set_ylabel('Temperatura (ºC)', fontsize=7)  # Tamanho do título do eixo y.
ax2.set_ylim(0, 30)  # Define o mínimo e máximo valor do eixo y.
ax2.set_yticks(np.arange(0, 35, step=5))  # Define o mínimo e máximo valor do eixo y, tamanho dos seus rótulos.
ax2.tick_params(labelsize=7)  # Tamanho dos seus rótulos do eixo y direito.

#  Formatação do eixo x.
plt.xticks(meses, fontsize=10)  # Rótulos do eixo x e tamanho.
plt.xlabel('Mês', fontsize=10)  # Tamanho do título do eixo x.

# Gera a legenda sem borda, define localização e o seu tamanho.
ax.legend(frameon =False, loc='upper left', fontsize=7, bbox_to_anchor=(0, 0.93))
ax2.legend(frameon =False, loc='upper left', fontsize=7)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex14.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)