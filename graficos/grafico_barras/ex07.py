import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc
import xarray as xr

# Abertura do arquivo.
ds = nc.Dataset('../../dados/netcdf/spi.nc')

maximo_valor_y = 3.0  # Máximo valor do eixo y.
minimo_valor_y = -2.5  # Mínimo valor do eixo y.
x = np.arange(21)  # Desde 01/2019 a 09/2020 = 21 meses.
datas = ['201901', '201902', '201903', '201904', '201905', '201906', '201907', '201908', '201909', '201910', '201911', '201912', '202001', '202002', '202003', '202004', '202005', '202006', '202007', '202008', '202009']

# Seleciona o SPI de interesse:
# Formato: spi(time, spi, lat, lon) = (492, 6, 1, 1)
# Valor  => spi = 1, 3, 6, 12, 24, 36 meses
# Índice => spi = 0, 1, 2,  3,  4,  5 
y = ds['spi'][468:489, 0, 0, 0]

# Separa os valores mínimos e máximos.
acima_limiar = np.maximum(y - 0, 0)
abaixo_limiar = np.minimum(y, 0)

fig, ax = plt.subplots(figsize=(6,3))  # Largura e altura da figura.

# Gera o plot com base nos limiares e separa o que é positivo (negativo) com vermelho (azul).
ax.bar(x, abaixo_limiar, 0.75, color="r", alpha=0.5)
ax.bar(x, acima_limiar, 0.75, color="b", bottom=abaixo_limiar, alpha=0.5)

plt.axhline(linestyle='--', y=2, linewidth=0.5, color='black')  # Linha no valor 2, espessura = 0.5 e cor = black.
plt.axhline(linestyle='--', y=1.5, linewidth=0.5, color='black')  # Linha no valor 1.5, espessura = 0.5 e cor = black.
plt.axhline(linestyle='--', y=1, linewidth=0.5, color='black')  # Linha no valor 1, espessura = 0.5 e cor = black.
plt.axhline(linestyle='-', y=0, linewidth=0.5, color='black')  # Linha no valor zero, espessura = 0.5 e cor = black.
plt.axhline(linestyle='--', y=-2, linewidth=0.5, color='black')  # Linha no valor -2, espessura = 0.5 e cor = black.
plt.axhline(linestyle='--', y=-1.5, linewidth=0.5, color='black')  # Linha no valor -1.5, espessura = 0.5 e cor = black.
plt.axhline(linestyle='--', y=-1, linewidth=0.5, color='black')  # Linha no valor -1, espessura = 0.5 e cor = black.

# Linhas horizontal dos valores positivos de SPI.
plt.text(-0.3, 2.05, 'Extremamente Úmido', fontsize=8)
plt.text(-0.3, 1.55, 'Muito Úmido', fontsize=8)
plt.text(-0.3, 1.05, 'Moderadamente Úmido', fontsize=8)
plt.text(-0.3, 0.80, 'Próximo do normal', fontsize=8)

# Linhas horizontal dos valores negativos de SPI.
plt.text(-0.3, -2.18, 'Extremamente seco', fontsize=8)
plt.text(-0.3, -1.68, 'Severamente seco', fontsize=8)
plt.text(-0.3, -1.18, 'Moderadamente seco', fontsize=8)
plt.text(-0.3, -0.92, 'Próximo do normal', fontsize=8)

# Título da figura.
plt.title('SPI no bioma Pantanal', fontsize=8)

#  Formatação do eixo x:
plt.xlim(-0.5, 20.5)  # Define o mínimo e o máximo valor do eixo x.
# Rótulos do eixo x, tamanho e orientação.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], datas, fontsize=8)

#  Formatação do eixo y:
plt.ylabel('SPI (Adimensional)', fontsize=8)  # Tamanho do título do eixo y.
plt.ylim(minimo_valor_y, maximo_valor_y-0.5)  # Define o mínimo e máximo valor do eixo y.
# Define o mínimo e máximo valor do eixo y, tamanho dos seus rótulos.
plt.yticks(np.arange(minimo_valor_y, maximo_valor_y, step=0.5), fontsize=8)  
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex07.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)