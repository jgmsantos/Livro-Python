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

#  Plota a barbela do vento. fill_empty = Onde o valor do vento for nulo, utiliza um círculo preenchido, 
#  length = tamanho da barbela, emptybarb = insere um círculo quando o vento for calmo, spacing = espaçamento entre as barbelas, 
#  height = altura das barbelas, flag = define a velocidade máxima da barbela. 
plt.barbs(lon, lat, u, v, fill_empty=True, length=5, sizes=dict(emptybarb=0.25, spacing=0.2, height=0.5), 
          barbcolor='black', barb_increments=dict(flag=50))

plt.tick_params(axis='y', right=True)  #  Habilita o tickmark do eixo direito.

#  Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex01.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)