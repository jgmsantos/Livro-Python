import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc


# Abertura do arquivo.
ds = nc.Dataset('../../dados/netcdf/rf.serie.julaout2020.nc')

x = np.arange(123)  # Desde 01/07/2020 a 31/10/2020 = 123 dias.

y = ds['rf'][:, 0, 0]

fig, ax = plt.subplots(figsize=(6,3))  # Largura e altura da figura.

# Gera o plot.
ax.plot(x, y, 
        color="black", 
        marker='o', 
        linestyle='solid', 
        linewidth=1, 
        markersize=2)

# Adiciona as linhas horizontais em cada posição y e define uma cor.
plt.axhline(linestyle='-', y=0.15, linewidth=0.5, color='darkgreen')
plt.axhline(linestyle='-', y=0.4, linewidth=0.5, color='lime')
plt.axhline(linestyle='-', y=0.70, linewidth=0.5, color='yellow')
plt.axhline(linestyle='-', y=0.95, linewidth=0.5, color='orange')
plt.axhline(linestyle='-', y=1, linewidth=0.5, color='red')

# Título da figura.
plt.title('Risco de Fogo: 01/07 a 31/10/2020', fontsize=10)

#  Formatação do eixo x:
plt.xlim(-1, 124)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
# Rótulos do eixo x, tamanho e orientação.
plt.xticks([0, 14, 31, 45, 62, 76, 92, 106, 122], 
           ['01Jul', '15Jul', '01Ago', 
            '15Ago', '01Set', '15Set', 
            '01Out', '15Out', '31Out'], 
           fontsize=9)  

#  Formatação do eixo y:
plt.ylabel('Risco de Fogo', fontsize=9)
plt.ylim(0, 1.1)
# Define o mínimo e máximo valor do eixo y e o tamanho dos seus rótulos.
plt.yticks([0.15, 0.40, 0.70, 0.95, 1], 
           ['Mínimo', 'Baixo', 'Médio', 'Alto', 'Crítico'], 
           fontsize=9)  
plt.tick_params(axis='y', right=True)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex04.jpg', transparent=True, dpi=300, bbox_inches='tight', 
            pad_inches=0)  