import pandas as pd
import matplotlib.pyplot as plt

# Leitura do arquivo.
df1 = pd.read_csv('../dados/texto/temperatura.txt', sep= '\t', names=['Mês', 'Climatologia', '2019', '2020'])
df2 = pd.read_csv('../dados/texto/precipitacao.txt', sep= '\t', names=['Mês', 'Climatologia', '2019', '2020'])

mes = df1['Mês']
tclima = df1['Climatologia']
t2020 = df1['2020']

pclima = df2['Climatologia']
p2020 = df2['2020']

nlin = 2  # 2 linhas.
ncol = 2  # 2 coluna.

# figsize define o tamanho e a largura da figura.
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nlin, ncol, figsize=(12,9))

# Plot de cada série de dados.
ax1.bar(mes, tclima, color='green', alpha=0.5, width=0.6)
ax2.bar(mes, t2020, color='red', alpha=0.5, width=0.6)
ax3.bar(mes, pclima, color='green', alpha=0.5, width=0.6)
ax4.bar(mes, p2020, color='red', alpha=0.5, width=0.6)

# Definição de variáveis.
tamanho_titulo_grafico=18
tamanho_titulo_figura=14
tamanho_titulo_x=14
tamanho_rotulo_x=14
tamanho_titulo_y=14
tamanho_rotulo_y=14
minimo_valor_y1=25
maximo_valor_y1=30
minimo_valor_y2=0
maximo_valor_y2=400

# Título principal da figura.
fig.suptitle('Variáveis meteorológicas', fontsize=tamanho_titulo_grafico)  

# Título de cada figura e o seu tamanho.
ax1.set_title('Climatologia de Temperatura', fontsize=tamanho_titulo_figura)
ax2.set_title('Temperatura: 2020', fontsize=tamanho_titulo_figura)
ax3.set_title('Climatologia de Precipitação', fontsize=tamanho_titulo_figura)
ax4.set_title('Precipitação: 2020', fontsize=tamanho_titulo_figura)

# Formatação do eixo x.
ax1.set_xlabel('Mês', fontsize=tamanho_titulo_x)  # Título do eixo x e o seu tamanho.
ax2.set_xlabel('Mês', fontsize=tamanho_titulo_x)  # Título do eixo x e o seu tamanho.
ax3.set_xlabel('Mês', fontsize=tamanho_titulo_x)  # Título do eixo x e o seu tamanho.
ax4.set_xlabel('Mês', fontsize=tamanho_titulo_x)  # Título do eixo x e o seu tamanho.

# Habilita o tickmark do eixo inferior e define o tamanho dos rótulos do eixo x inferior.
ax1.tick_params(axis='x', top=True, labelsize=tamanho_rotulo_x)  
ax2.tick_params(axis='x', top=True, labelsize=tamanho_rotulo_x)
ax3.tick_params(axis='x', top=True, labelsize=tamanho_rotulo_x)
ax4.tick_params(axis='x', top=True, labelsize=tamanho_rotulo_x)

# Formatação do eixo y.
ax1.set_ylabel('Temperatura (ºC)', fontsize=tamanho_titulo_y)  # Título do eixo y e o seu tamanho.
ax2.set_ylabel('Temperatura (ºC)', fontsize=tamanho_titulo_y)  # Título do eixo y e o seu tamanho.
ax3.set_ylabel('Precipitação (mm/mês)', fontsize=tamanho_titulo_y)  # Título do eixo y e o seu tamanho.
ax4.set_ylabel('Precipitação (mm/mês)', fontsize=tamanho_titulo_y)  # Título do eixo y e o seu tamanho.

# Habilita o tickmark do eixo direito e define o tamanho dos rótulos do eixo y esquerdo.
ax1.tick_params(axis='y', right=True, labelsize=tamanho_rotulo_y)  
ax2.tick_params(axis='y', right=True, labelsize=tamanho_rotulo_y)
ax3.tick_params(axis='y', right=True, labelsize=tamanho_rotulo_y)
ax4.tick_params(axis='y', right=True, labelsize=tamanho_rotulo_y)

# Define os valores mínimo e máximo do eixo y de cada ax.
ax1.set_ylim(minimo_valor_y1, maximo_valor_y1)
ax2.set_ylim(minimo_valor_y1, maximo_valor_y1)
ax3.set_ylim(minimo_valor_y2, maximo_valor_y2)
ax4.set_ylim(minimo_valor_y2, maximo_valor_y2)

# Define os rótulo que vão aparecer no eixo y.
ax1.set_yticks(ticks=[25, 26, 27, 28, 29, 30])
ax2.set_yticks(ticks=[25, 26, 27, 28, 29, 30])
ax3.set_yticks(ticks=[0, 100, 200, 300, 400])
ax4.set_yticks(ticks=[0, 100, 200, 300, 400])

fig.tight_layout()  # Ajusta automaticamente os espaços entre as figuras.

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex03.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)