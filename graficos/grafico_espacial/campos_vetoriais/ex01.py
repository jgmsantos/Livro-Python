import matplotlib.pyplot as plt
import proplot as plot
import xarray as xr

from cartopy.feature import NaturalEarthFeature


# Abertura do arquivo com o xarray.
dsu = xr.open_dataset('../../../dados/netcdf/uwnd.nc')
dsv = xr.open_dataset('../../../dados/netcdf/vwnd.nc')

# Importando as variáveis.
u = dsu['uwnd'][0,9,:,:]
v = dsv['vwnd'][0,9,:,:]
lat = dsu['lat']
lon = dsu['lon']

# Linhas do continente/estados do Brasil.
estados = NaturalEarthFeature(category="cultural", scale="50m", facecolor="none",
                              name="admin_1_states_provinces_shp")


fig, ax = plot.subplots(axwidth=5, tight=True, proj='pcarree')

# Formatação do mapa.
ax.format(coast=True, borders=True, innerborders=True,
          labels=True, grid=False, latlines=10, lonlines=5,
          latlim=(-60, 10), lonlim=(-90, -30),
          small='13px', large='17px',
          title='Velocidade do vento em 200 hPa')

# Plota a barbela do vento. fill_empty = Onde o valor do vento for nulo, 
# utiliza um círculo preenchido, length = tamanho da barbela, 
# emptybarb = insere um círculo quando o vento for calmo, 
# height = altura das barbelas, flag = define a velocidade 
# máxima da barbela.
plt.barbs(lon, lat, u, v, fill_empty=True, length=5, sizes=dict(emptybarb=0.2, 
          height=0.4), barbcolor='black', barb_increments=dict(flag=30))

# Adiciona o contorno dos estados e países.
ax.add_feature(estados, linewidth=0.5, edgecolor="k")

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex01.jpg', transparent=True, dpi=300, 
            bbox_inches='tight', pad_inches=0.1)