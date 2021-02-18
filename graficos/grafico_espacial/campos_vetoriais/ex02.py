import matplotlib.pyplot as plt
import xarray as xr

#  Abertura do arquivo com o xarray.
dsu = xr.open_dataset('../../../dados/netcdf/uwnd.nc')
dsv = xr.open_dataset('../../../dados/netcdf/vwnd.nc')

#  Importando variáveis.
u = dsu['uwnd'][0,9,:,:]
v = dsv['vwnd'][0,9,:,:]
lat = dsu['lat']
lon = dsu['lon']

#  Plota o vetor do vento. headwidth = tamanho da ponta do vetor, headlength = comprimento da ponta do vetor, 
#  color = cor dos vetores.
vetor = plt.quiver(lon, lat, u, v, headwidth=4, headlength=5, color='black')
#  Posição x, y onde desenhar o vetor, 30 = unidade (m/s) que representa o vetor, r'$30 \frac{m}{s}$' = texto que vai aparecer na 
#  figura, labelpos = em qual posição do vetor deve-se adicionar o label, coordinates = qual eixo deve-se inserir o label.
vetorkey = plt.quiverkey(vetor, 0.83, 0.9, 30, r'$30 \frac{m}{s}$', labelpos='E', coordinates='figure')
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex02.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)

plt.show()  