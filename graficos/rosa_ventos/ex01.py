from windrose import WindroseAxes
from windrose import WindAxes
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# Abertura do arquivo vento_velocidade_direcao.txt com o separador TAB. Adiciona também o título de cada coluna.
# O arquivo tem formato de 123 linhas por 3 colunas. A primeira coluna é a data, a segunda, a velocidade e a  
# a terceria, a direção do vento.
df = pd.read_csv('../../dados/texto/variaveis_meteorologicas.txt', sep= '\t', names=['Data', 'Umidade Relativa', 'Temperatura', 'Precipitacao', 'Velocidade', 'Direcao'])

velocidade = df['Velocidade']  # Importa a velocidade do vento (m/s).
direcao_graus = df['Direcao']  # Importa a direção do vento (graus).

ax = WindroseAxes.from_ax()

# normed = normaliza os dados para mostrar em porcentagemTrue, opening = largura das pétalas da rosa dos ventos, 
# edgecolor = cor da borda das pétalas, alpha = aplica efeito de transparência na cor.
x = ax.bar(direcao_graus, velocidade, normed=True, opening=0.8, edgecolor='black', bins=5, alpha=0.5)

# Configuração da rosa dos ventos.
ax.set_legend(frameon=True, loc='lower left', title='(m/s)', bbox_to_anchor=(0.55, 0.1), fontsize=15)
ax.set_theta_zero_location("N")  # Define a referência da figura.
ax.set_theta_direction(-1)  # Rotaciona a figura para ficar correta.
ax.set_theta_offset(2.36)  # Rotaciona o círculo.
ax.set_xticklabels(['NW', 'N', 'NE', 'E', 'SE', 'S', 'SW', 'W'], fontsize=15)  # Suporta até 8 rótulos.

# Formatação do título da figura.
plt.title("Direção predominante do vento e velocidade", y=1.08, fontsize=15)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex01.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)