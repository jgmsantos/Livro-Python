import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Abertura do arquivo utilizando o separador espaço e adicionando título como primeira linha.
df = pd.read_csv('../../dados/texto/variaveis_meteorologicas.txt', sep= '\t', names=['Data','UR', 'TEMP', 'PREC', 'VEL_VENTO', 'DIR_VENTO'])

x = np.arange(123)  # Desde 01/07/2020 31/10/2020 = 123 dias.
dias = ['01/07/2020', '15/07/2020', '01/08/2020', '15/08/2020', '01/09/2020', '15/09/2020', '01/10/2020', '15/10/2020', '31/10/2020']

ur = df['UR']
temp = df['TEMP']

# Gera o plot com base nos limiares e separa o que é positivo (negativo) com vermelho (azul).
fig, ax = plt.subplots(figsize=(6,3))  # Largua e altura da figura.

# Plot do gráfico de barra.
ax.bar(x, ur, 0.75, color="blue", alpha=0.5, label='Precipitação')

ax2 = ax.twinx()

# Plot do gráfico de linha.
ax2.plot(x, temp, color="chocolate", alpha=0.5, label='Temperatura')

# Título da figura.
plt.title('Umidade Relativa e Temperatura: Serra do Cipó', fontsize=10)

#  Formatação do eixo y esquerdo.
ax.set_ylabel('Precipitação (mm/dia)', fontsize=7)  # Tamanho do título do eixo y.
ax.set_ylim(0, 100)  # Define o mínimo e máximo valor do eixo y.
ax.set_yticks(np.arange(0, 105, step=10))  # Define o mínimo e máximo valor do eixo y.
ax.tick_params(labelsize=7)  # Tamanho dos seus rótulos do eixo y esquerdo.

#  Formatação do eixo y direito.
ax2.set_ylabel('Temperatura (ºC)', fontsize=7)  # Tamanho do título do eixo y.
ax2.set_ylim(10, 35)  # Define o mínimo e máximo valor do eixo y.
ax2.set_yticks(np.arange(10, 40, step=5))  # Define o mínimo e máximo valor do eixo y, tamanho dos seus rótulos.
ax2.tick_params(labelsize=7)  # Tamanho dos seus rótulos do eixo y direito.

#  Formatação do eixo x.
ax.set_xlim(-1, 123, 1)  # Define o mínimo e o máximo valor do eixo x.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
plt.xticks([0, 14, 31, 45, 62, 76, 92, 106, 122], dias, fontsize=7)  # Rótulos do eixo x, tamanho e orientação.

# Gera a legenda sem borda, define localização e o seu tamanho.
ax.legend(frameon =False, loc='upper left', fontsize=7, bbox_to_anchor=(0, 0.92))
ax2.legend(frameon =False, loc='upper left', fontsize=7)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex12.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)  