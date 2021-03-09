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

# Tamanho e altura da figura.
fig = plt.figure(figsize=(9, 6))

nlin = 3  # 2 linhas.
ncol = 2  # 2 coluna.

# Define quantas figuras serão geradas.
gs = gridspec.GridSpec(nlin, ncol, width_ratios=(3, 3), height_ratios=(3, 3, 3))

# Plot de cada série de dados e sua posição na figura.
ax1 = fig.add_subplot(gs[0, 0])
ax1.bar(mes, ur, color='green', alpha=0.5, width=0.6)

ax2 = fig.add_subplot(gs[0, 1])
ax2.bar(mes, temp, color='red', alpha=0.5, width=0.6)

ax3 = fig.add_subplot(gs[1, 0])
ax3.bar(mes, vel, color='orange', alpha=0.5, width=0.6)

ax4 = fig.add_subplot(gs[1, 1])
ax4.bar(mes, dir, color='blue', alpha=0.5, width=0.6)

ax5 = fig.add_subplot(gs[2:, :-1])
ax5.bar(mes, tempk, color='gray', alpha=0.5, width=0.6)

# Ajusta automaticamente os espaços entre as figuras.
plt.tight_layout()

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex06.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)