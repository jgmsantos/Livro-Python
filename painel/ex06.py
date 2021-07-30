import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.gridspec as gridspec

# Leitura do arquivo.
df = pd.read_csv('../dados/texto/ERA5.Climatologia.txt', 
                 sep= '\t', 
                 names=['Mês', 'Umidade Relativa', 'Temperatura', 'VelVento', 'DirVento'])

mes = df['Mês']
ur = df['Umidade Relativa']
temp = df['Temperatura']
vel = df['VelVento']
dir = df['DirVento']
tempk = temp + 273.15  # Conversão de Celsius para Kelvin.

# Largura e altura da figura.
fig = plt.figure(figsize=(9, 7))

# Espaçamento horizontal e vertical entre as figuras.
plt.subplots_adjust(wspace=0.3, hspace=0.5)

# Plot das figuras.
ax1 = plt.subplot2grid((3, 2), (0, 0))
ax1.bar(mes, ur, color='green', alpha=0.5, width=0.6)

ax2 = plt.subplot2grid((3, 2), (0, 1))
ax2.bar(mes, temp, color='red', alpha=0.5, width=0.6)

ax3 = plt.subplot2grid((3, 2), (1, 0))
ax3.bar(mes, vel, color='orange', alpha=0.5, width=0.6)

ax4 = plt.subplot2grid((3, 2), (1, 1))
ax4.bar(mes, dir, color='blue', alpha=0.5, width=0.6)

ax5 = plt.subplot2grid((3, 8), (2, 2), colspan=4)
ax5.bar(mes, tempk, color='gray', alpha=0.5, width=0.6)

# Título principal da figura.
plt.suptitle('Variáveis meteorológicas', fontsize=9, y=0.96)

# Título de cada figura e o seu tamanho.
ax1.set_title('Umidade Relativa', fontsize=9)
ax2.set_title('Temperatura', fontsize=9)
ax3.set_title('Velocidade do vento', fontsize=9)
ax4.set_title('Direção do vento', fontsize=9)
ax5.set_title('Temperatura em Kelvin', fontsize=9)

# Tamanho dos rótulos do eixo x inferior.
ax1.tick_params(labelsize=9)  
ax2.tick_params(labelsize=9)
ax3.tick_params(axis='x', labelsize=9)
ax4.tick_params(axis='x', labelsize=9)
ax5.tick_params(axis='x', labelsize=9)

# Título do eixo y e o seu tamanho.
ax1.set_ylabel('UR (%)', fontsize=9)
ax2.set_ylabel('TEMPC (ºC)', fontsize=9)
ax3.set_ylabel('VEL (m/s)', fontsize=9)
ax4.set_ylabel('DIR (graus)', fontsize=9)
ax5.set_ylabel('TEMPK (K)', fontsize=8)

# Define os valores mínimo e máximo do eixo y de cada ax.
ax1.set_ylim(40, 100)
ax2.set_ylim(16, 24)
ax3.set_ylim(0, 2)
ax4.set_ylim(0, 100)
ax5.set_ylim(280, 300)

# Define os rótulo que vão aparecer no eixo y.
ax1.set_yticks(ticks=[40, 60, 80, 100])
ax2.set_yticks(ticks=[16, 18, 20, 22, 24])
ax3.set_yticks(ticks=[0, 0.5, 1.0, 1.5, 2.0, 2.5])
ax4.set_yticks(ticks=[0, 25, 50, 75, 100])
ax5.set_yticks(ticks=[280, 285, 290, 295, 300])

# Tamanho dos rótulos do eixo y esquerdo.
ax1.tick_params(axis='y', right=True, labelsize=9)
ax2.tick_params(axis='y', right=True, labelsize=9)
ax3.tick_params(axis='y', right=True, labelsize=9)
ax4.tick_params(axis='y', right=True,labelsize=9)
ax5.tick_params(axis='y', right=True,labelsize=9)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex06.jpg', transparent=True, dpi=300, bbox_inches='tight', 
             pad_inches=0)