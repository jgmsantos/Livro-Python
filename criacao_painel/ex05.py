import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Leitura do arquivo.
df = pd.read_csv('../dados/texto/ERA5.Climatologia.txt', sep= '\t', names=['Mês', 'Umidade Relativa', 'Temperatura', 'VelVento', 'DirVento'])

mes = df['Mês']
ur = df['Umidade Relativa']
temp = df['Temperatura']
vel = df['VelVento']
dir = df['DirVento']
tempk = temp + 273.15  # De Celsius para Kelvin.

# O figsize define o tamanho e a largura da figura.
plt.figure(figsize=(6, 4))

nlin = 3  # 2 linhas.
ncol = 3  # 2 coluna.

# Define quantas figuras serão geradas.
gs = gridspec.GridSpec(nlin, ncol)

# Plot de cada série de dados e sua posição na figura.
ax1 = plt.subplot(gs[0, :])
ax1.bar(mes, ur, color='green', alpha=0.5, width=0.6)

ax2 = plt.subplot(gs[1, :-1])
ax2.bar(mes, temp, color='red', alpha=0.5, width=0.6)

ax3 = plt.subplot(gs[1:, -1])
ax3.bar(mes, tempk, color='gray', alpha=0.5, width=0.6)

ax4 = plt.subplot(gs[-1, 0])
ax4.bar(mes, dir, color='blue', alpha=0.5, width=0.6)

ax5 = plt.subplot(gs[-1, -2])
ax5.bar(mes, vel, color='orange', alpha=0.5, width=0.6)

# Título principal da figura.
plt.suptitle('Variáveis meteorológicas', fontsize=7)  

# Título de cada figura e o seu tamanho.
ax1.set_title('Umidade Relativa', fontsize=7)
ax2.set_title('Temperatura', fontsize=7)
ax3.set_title('Temperatura em Kelvin', fontsize=7)
ax4.set_title('Direção do vento', fontsize=7)
ax5.set_title('Velocidade do vento', fontsize=7)

# Tamanho dos rótulos do eixo x inferior.
ax1.tick_params(labelsize=7)  
ax2.tick_params(labelsize=7)
ax3.tick_params(axis='x', labelsize=5, rotation=90)
ax4.tick_params(axis='x', labelsize=5, rotation=90)
ax5.tick_params(axis='x', labelsize=5, rotation=90)

# Título do eixo y e o seu tamanho.
ax1.set_ylabel('UR (%)', fontsize=7)
ax2.set_ylabel('TEMPC (ºC)', fontsize=7)
ax3.set_ylabel('TEMPK (K)', fontsize=7)
ax4.set_ylabel('DIR (grau)', fontsize=7)
ax5.set_ylabel('VEL (m/s)', fontsize=7)

# Define os valores mínimo e máximo do eixo y de cada ax.
ax1.set_ylim(40, 100)
ax2.set_ylim(16, 24)
ax3.set_ylim(280, 300)
ax4.set_ylim(0, 100)
ax5.set_ylim(0, 2)

# Define os rótulo que vão aparecer no eixo y.
ax1.set_yticks(ticks=[40, 60, 80, 100])
ax2.set_yticks(ticks=[16, 18, 20, 22, 24])
ax3.set_yticks(ticks=[280, 285, 290, 295, 300])
ax4.set_yticks(ticks=[0, 25, 50, 75, 100])
ax5.set_yticks(ticks=[0, 0.5, 1.0, 1.5, 2.0, 2.5])

# Tamanho dos rótulos do eixo y esquerdo.
ax1.tick_params(axis='y', right=True, labelsize=7)
ax2.tick_params(axis='y', right=True, labelsize=7)
ax3.tick_params(axis='y', right=True, labelsize=7)
ax4.tick_params(axis='y', right=True,labelsize=7)
ax5.tick_params(axis='y', right=True,labelsize=7)

# Ajusta automaticamente os espaços entre as figuras.
plt.tight_layout()

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex05.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)