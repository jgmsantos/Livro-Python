from windrose import WindroseAxes
from windrose import WindAxes
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

# normed = normaliza os dados para mostrar em porcentagemTrue, opening = largura das pétalas da rosa dos ventos, 
# edgecolor = cor da borda das pétalas, alpha = aplica efeito de transparência na cor.
x = ax.bar(direcao_graus, velocidade, normed=True, opening=0.8, edgecolor='black', bins=5, alpha=0.5)

# Configuração da rosa dos ventos.
ax.set_legend(frameon=True, loc='lower left', title='m/s')
ax.set_theta_zero_location("N")  # Define a referência da figura.
ax.set_theta_direction(-1)  # Rotaciona a figura para ficar correta.
ax.set_xticklabels(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])  # Suporta até 8 rótulos.

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex01.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)