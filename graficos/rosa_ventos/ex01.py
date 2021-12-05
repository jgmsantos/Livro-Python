from windrose import WindroseAxes
from matplotlib import pyplot as plt
import pandas as pd


# Abertura do arquivo variaveis_meteorologicas.txt com o separador TAB. 
# Adiciona também o título de cada coluna.
df = pd.read_csv('../../dados/texto/variaveis_meteorologicas.txt', 
                 sep= '\t', 
                 names=['Data', 'Umidade Relativa', 'Temperatura', 
                        'Precipitacao', 'Velocidade', 'Direcao'])

velocidade = df['Velocidade']  # Importa a velocidade do vento (m/s).
direcao_graus = df['Direcao']  # Importa a direção do vento (graus).

ax = WindroseAxes.from_ax()

# normed = True normaliza os dados para mostrar em porcentagem, 
# opening = largura das pétalas da rosa dos ventos, edgecolor = cor da 
# borda das pétalas, bins = número de intervalos da velocidade do vento, 
# alpha = aplica efeito de transparência na cor.
x = ax.bar(direcao_graus, 
           velocidade, 
           normed=True, 
           opening=0.8, 
           edgecolor='black', 
           bins=4, 
           alpha=0.5)

# Configuração da rosa dos ventos.
ax.set_legend(frameon=True, 
              loc='lower left', 
              title='(km/h)', 
              bbox_to_anchor=(0.55, 0.1), 
              fontsize=20)
ax.set_theta_zero_location("E")  # Define a direção do vento como referência.
ax.set_xticklabels(['E','NE','N','NW','W','SW','S','SE'], 
                    fontsize=15)

# Formatação do título da figura.
plt.title("Direção predominante e velocidade do vento - 2003 a 2020", 
          y=1.08, 
          fontsize=15)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex01.jpg', transparent=True, dpi=300, bbox_inches='tight', 
            pad_inches=0)