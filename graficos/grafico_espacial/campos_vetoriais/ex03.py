import matplotlib.pyplot as plt
import xarray as xr
import numpy as np

#  Abertura do arquivo com o xarray.
dsu = xr.open_dataset('../../../dados/netcdf/uwnd.nc')
dsv = xr.open_dataset('../../../dados/netcdf/vwnd.nc')

#  Importando variáveis.
u = dsu['uwnd'][0,9,:,:]  # Primeiro tempo, último nível vertical, todas as lat e lon.
v = dsv['vwnd'][0,9,:,:]
vel = np.sqrt(u*u + v*v)  # Calcula a velocidade do vento (m/s).
lat = dsu['lat']  # Importanto as coordenadas de lat
lon = dsu['lon']  # e lon.

#  Plota o vetor do vento e sua magnitude (vel). headwidth = tamanho da ponta do vetor, headlength = comprimento da ponta do vetor, 
#  color = cor dos vetores.
vetor = plt.quiver(lon, lat, u, v, vel, headwidth=4, headlength=5, color='black')
#  Posição x, y onde desenhar o vetor, 30 = unidade (m/s) que representa o vetor, r'$30 \frac{m}{s}$' = texto que vai aparecer na 
#  figura, labelpos = em qual posição do vetor deve-se adicionar o label, coordinates = qual eixo deve-se inserir o label.
vetorkey = plt.quiverkey(vetor, 0.79, 0.9, 30, r'$30m.s^{-1}$', labelpos='E', coordinates='figure')
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

#  Título principal da figura e tamanho.
plt.title('Vento em 200hPa', fontsize=10)

#  Formatação do eixo x e tamanho.
plt.xlabel('Longitude', fontsize=9)  # Define o tamanho do título do eixo x.
plt.xticks(fontsize=8)  # Define o tamanho dos rótulos do eixo x.

#  Formatação do eixo y e tamanho.
plt.ylabel('Latitude', fontsize=9)  # Define o tamanho do título do eixo y.
plt.yticks(fontsize=8)  # Define o tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

# Gera a barra de corres, format = formata os valores, shrink = tamanho da barra de cores, orientation = orientação da barra, 
# pad = proximidade do eixo x inferior.
cbar = plt.colorbar(format='%.0f', shrink=1, orientation='horizontal', pad=0.15)
cbar.set_label('(m/s)')  # Unidade da barra de cores.

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex03.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)

plt.show()