from windrose import WindroseAxes
from windrose import WindAxes
from windrose import windrose
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# Abertura do arquivo temperatura.txt com o separador TAB. Adiciona também o título de cada coluna.
# O arquivo tem formato de 12 linhas por 4 colunas. A primeira coluna é o mês, a segunda, a climatologia, 
# a terceria, o ano de 2019 e a quarta, o ano de 2020.
# Utiliza o separador '\t' que quer dizer TAB e cria o título para cada uma das colunas.
df = pd.read_csv('../../dados/texto/vento_velocidade_direcao.txt', sep= '\t', names=['Data', 'Velocidade', 'Direcao Graus'])

velocidade = df['Velocidade']  # Importa a velocidade do vento (m/s).
direcao_graus = df['Direcao Graus']  # Importa a direção do vento em graus.

ax = WindroseAxes.from_ax()

# Frequência de cada direção do vento para todas as velocidades.
ax.bar(direcao_graus, velocidade, normed=True, nsector=16)
table = ax._info['table']
wd_freq = np.sum(table, axis=0)

# Geração do gráfico de barras com as frequências.
direction = ax._info['dir']
wd_freq = np.sum(table, axis=0)

print(wd_freq)
print(np.arange(16))

plt.bar(np.arange(16), wd_freq, align='center', left=0)  # Plot da figura de barras.

# Formatação do eixo x.
xlabels = ('N','','N-E','','E','','S-E','','S','','S-O','','O','','N-O','')
xticks=arange(16)
gca().set_xticks(xticks)
draw()
gca().set_xticklabels(xlabels)
draw()

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex02.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)