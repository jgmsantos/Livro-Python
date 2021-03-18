import pandas as pd
import matplotlib.pyplot as plt

# Leitura do arquivo.
df = pd.read_csv('../dados/texto/temperatura.txt', sep= '\t', names=['Mês', 'Climatologia', '2019', '2020'])

mes = df['Mês']
pclima = df['Climatologia']
p2019 = df['2019']
p2020 = df['2020']

nlin = 3  # 3 linhas.
ncol = 1  # 1 coluna.

# O figsize define o tamanho e a largura da figura.
fig, (ax1, ax2, ax3) = plt.subplots(nlin, ncol, figsize=(4, 4))

# Plot de cada série de dados.
ax1.bar(mes, pclima)
ax2.bar(mes, p2019)
ax3.bar(mes, p2020)

fig.suptitle('Temperatura', fontsize=8)

# Título de cada figura.
ax1.set_title('Clima', fontsize=8)
ax2.set_title('2019', fontsize=8)
ax3.set_title('2020', fontsize=8)

# Define os valores mínimo e máximo do eixo y de cada ax.
ax1.set_ylim(25, 30)
ax2.set_ylim(25, 30)
ax3.set_ylim(25, 30)

ax1.tick_params(labelsize=8)
ax2.tick_params(labelsize=8)
ax3.tick_params(labelsize=8)

fig.tight_layout()

# Habilita o tickmark do eixo direito.
ax1.tick_params(axis='y', right=True)  
ax2.tick_params(axis='y', right=True)
ax3.tick_params(axis='y', right=True)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex01.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)