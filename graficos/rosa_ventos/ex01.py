from windrose import WindroseAxes
from windrose import WindAxes
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# Abertura do arquivo variaveis_meteorologicas.txt com o separador TAB. Adiciona também o título de cada coluna.
df = pd.read_csv('../../dados/texto/variaveis_meteorologicas.txt', sep= '\t', names=['Data', 'Umidade Relativa', 'Temperatura', 'Precipitacao', 'Velocidade', 'Direcao'])

velocidade = df['Velocidade']  # Importa a velocidade do vento (m/s).
direcao_graus = df['Direcao']  # Importa a direção do vento (graus).

ax = WindroseAxes.from_ax()

# normed = normaliza os dados para mostrar em porcentagemTrue, opening = largura das pétalas da rosa dos ventos, 
# edgecolor = cor da borda das pétalas, bins = número de intervalos da velocidad do vento, alpha = aplica efeito de transparência na cor.
x = ax.bar(direcao_graus, velocidade, normed=True, opening=0.8, edgecolor='black', bins=4, alpha=0.5)

# Configuração da rosa dos ventos.
ax.set_legend(frameon=True, loc='lower left', title='(km/h)', bbox_to_anchor=(0.55, 0.1), fontsize=20)
ax.set_theta_zero_location("E")  # Define a referência da figura.
#ax.set_rmax(70)  # Define o máximo valor em porcentagem.
#ax.set_rmin(0)  # Define o mínimo valor em porcentagem.
#ax.set_rticks(np.arange(0, 100, 20))  # Intervalos da rosa dos ventos. Variando de 0 a 90%.
#ax.set_xticklabels(['E','NE','N','NW','W','SW','S','SE'], fontsize=15)  # Suporta até 8 rótulos.
ax.set_xticklabels(['E','NE','N','NW','W','SW','S','SE'], fontsize=15)  # Suporta até 8 rótulos.

# Formatação do título da figura.
plt.title("Direção predominante e velocidade do vento - 2003 a 2020", y=1.08, fontsize=15)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex01.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)