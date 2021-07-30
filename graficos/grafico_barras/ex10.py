import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Abertura do arquivo utilizando o separador espaço e adiciona o título 
# como primeira linha.
df1 = pd.read_csv('../../dados/texto/ERA5.Climatologia.txt', 
                  sep='\t', 
                  names=['Mês','UR', 'TEMP', 'VEL', 'DIR'])
df2 = pd.read_csv('../../dados/texto/precipitacao.txt', 
                  sep='\t', 
                  names=['Mês', 'Clima', '2019', '2020'])

meses = df1['Mês']  # Nome dos rótulos que vão aparecer no eixo x.
ur = df1['UR']
temp = df1['TEMP']
prec = df2['Clima']

fig, ax = plt.subplots(figsize=(6,3))  # Largura e altura da figura.

twin1 = ax.twinx()  # Qual eixo copiar? 
twin2 = ax.twinx()  # No caso, o eixo x.

# Distância do eixo y2 em relação ao y1.
twin2.spines.right.set_position(("axes", 1.15))

# Plot do gráfico de barra.
p1 = ax.bar(meses, prec, 0.35, color="blue", alpha=0.5, label='Precipitação')

# Plota do eixo esquerdo do gráfico de linha (Umidade Relativa).
p2, = twin1.plot(meses, 
                 ur, 
                 color="green", 
                 marker='o', 
                 linestyle='solid', 
                 linewidth=2, 
                 markersize=5, 
                 alpha=0.5, 
                 label='Umidade Relativa')

# Plota do eixo direito do gráfico de linha (Temperatura).
p3, = twin2.plot(meses, 
                 temp, 
                 color="red", 
                 marker='o', 
                 linestyle='solid', 
                 linewidth=2, 
                 markersize=5,
                 alpha=0.5, 
                 label='Temperatura')

# Título da figura.
plt.title('Média Mensal - 2003 a 2020', fontsize=8)

#  Formatação do eixo x.
ax.set_xlabel('Mês', fontsize=8)  # Tamanho do título do eixo x.
ax.tick_params('x', labelsize=8)

# Formatação do eixo y esquerdo (Precipitação).
ax.set_ylabel('Precipitação (mm/mês)', fontsize=8, color="blue")
ax.set_ylim(0, 300)
ax.set_yticks(np.arange(0, 310, 50))
ax.tick_params('y', labelsize=8, colors='blue')

# Formatação do eixo y direito (Umidade Relativa).
twin1.set_ylabel('Umidade Relativa (%)', fontsize=8, color='green')
twin1.set_ylim(40, 100)
twin1.set_yticks(np.arange(40, 110, 10))
twin1.tick_params('y', labelsize=8, colors='green')

# Formatação do eixo y direito (Temperatura).
twin2.set_ylabel('Temperatura (ºC)', fontsize=8, color='red')
twin2.set_ylim(16, 24)
twin2.set_yticks(np.arange(16, 25, 1))
twin2.tick_params('y', labelsize=8, colors='red')

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex10.jpg', transparent=True, dpi=300, bbox_inches='tight', 
            pad_inches=0)