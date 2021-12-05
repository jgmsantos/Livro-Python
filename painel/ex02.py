import pandas as pd
import matplotlib.pyplot as plt

# Leitura do arquivo.
df = pd.read_csv('../dados/texto/temperatura.txt', 
                 sep= '\t', 
                 names=['Mês', 'Climatologia', '2019', '2020'])

mes = df['Mês']
pclima = df['Climatologia']
p2019 = df['2019']
p2020 = df['2020']

nlin = 3  # 3 linhas.
ncol = 1  # 1 coluna.

# O figsize define o tamanho e a largura da figura.
fig, (ax1, ax2, ax3) = plt.subplots(nlin, ncol, figsize=(8, 9))

# Plot de cada série de dados.
ax1.bar(mes, pclima, color='green', alpha=0.5, width=0.6)
ax2.bar(mes, p2019, color='red', alpha=0.5, width=0.6)
ax3.bar(mes, p2020, color='orange', alpha=0.5, width=0.6)

# Título principal da figura.
fig.suptitle('Temperatura', fontsize=14)  

# Título de cada figura e o seu tamanho.
ax1.set_title('Climatologia', fontsize=14)
ax2.set_title('2019', fontsize=14)
ax3.set_title('2020', fontsize=14)

# Formatação do eixo x.
ax1.set_xlabel('Mês', fontsize=14)
ax2.set_xlabel('Mês', fontsize=14)
ax3.set_xlabel('Mês', fontsize=14)

# Habilita o tickmark do eixo inferior e define o 
# tamanho dos rótulos do eixo x inferior.
ax1.tick_params(axis='x', top=True, labelsize=14)  
ax2.tick_params(axis='x', top=True, labelsize=14)
ax3.tick_params(axis='x', top=True, labelsize=14)

# Formatação do eixo y.
ax1.set_ylabel('Temperatura (ºC)', fontsize=14)
ax2.set_ylabel('Temperatura (ºC)', fontsize=14)
ax3.set_ylabel('Temperatura (ºC)', fontsize=14)

# Habilita o tickmark do eixo direito e define o 
# tamanho dos rótulos do eixo y esquerdo.
ax1.tick_params(axis='y', right=True, labelsize=14)  
ax2.tick_params(axis='y', right=True, labelsize=14)
ax3.tick_params(axis='y', right=True, labelsize=14)

# Define os valores mínimo e máximo do eixo y de cada ax.
ax1.set_ylim(25, 30)
ax2.set_ylim(25, 30)
ax3.set_ylim(25, 30)

# Define os rótulos que vão aparecer no eixo y.
ax1.set_yticks(ticks=[25, 26, 27, 28, 29, 30])
ax2.set_yticks(ticks=[25, 26, 27, 28, 29, 30])
ax3.set_yticks(ticks=[25, 26, 27, 28, 29, 30])

fig.tight_layout()  # Ajusta automaticamente os espaços entre as figuras.

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex02.jpg', transparent=True, dpi=300, bbox_inches='tight', 
            pad_inches=0)