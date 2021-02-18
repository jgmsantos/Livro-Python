import matplotlib.pyplot as plt
import xarray as xr
from matplotlib.cm import get_cmap

fig, ax = plt.subplots(figsize=(3,3))  #  Define o tamanho da figura.

#  Abertura do arquivo com o xarray.
ds = xr.open_dataset('../../../dados/netcdf/TMED.CPTEC.CLIMA.amazonia.nc', decode_times=False)

#  Seleciona o primeiro tempo e visualiza a variável. O plt.contourf, o campo preenchido.
plt.contourf(ds['lon'], ds['lat'], ds['tmed'][0,:,:], cmap=get_cmap("jet"), levels=[25, 25.5, 26, 26.5, 27, 27.5, 28, 28.5, 29])

#  Título principal da figura e tamanho.
plt.title('Temperatura no bioma Amazônia', fontsize=8)

#  Formatação do eixo x e tamanho.
plt.xlabel('Longitude', fontsize=7)  #  Define o tamanho do título do eixo x.
plt.xticks(fontsize=7)  #  Define o tamanho dos rótulos do eixo x.

#  Formatação do eixo y e tamanho.
plt.ylabel('Latitude', fontsize=7)  #  Define o tamanho do título do eixo y.
plt.yticks(fontsize=7)  #  Define o tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  #  Habilita o tickmark do eixo direito.

#  Gera a barra de corres, sua orientação, proximidade (pad) do eixo x inferior e valores de temperatura definidos pelo usuário.
cbar = plt.colorbar(ax = ax, shrink=0.98, orientation='horizontal', pad=0.17, ticks=[25, 25.5, 26, 26.5, 27, 27.5, 28, 28.5, 29])
cbar.ax.tick_params(labelsize=6)  # Tamanho dos rótulos da barra de cores.

#  Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex01.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)