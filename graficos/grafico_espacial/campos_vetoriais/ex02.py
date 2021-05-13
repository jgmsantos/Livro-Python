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

# Plota o vetor do vento. headwidth = tamanho da ponta do vetor, 
# headlength = comprimento da ponta do vetor, color = cor dos vetores.
vetor = ax.quiver(lon, lat, u, v, headwidth=6, headlength=6, 
                  color='black', scale=8, scale_units='xy')

# Posição x, y onde desenhar o vetor, 30 = unidade (m/s) que representa 
# o vetor, r'$30 \frac{m}{s}$' = texto que vai aparecer na figura, 
# labelpos = em qual posição do vetor deve-se adicionar o label, 
# coordinates = qual eixo deve-se inserir o label.
vetorkey = ax.quiverkey(vetor, 0.94, 0.97, 30, r'$30\ m.s^{-1}$', 
                        labelpos='N', coordinates='figure', 
                        labelsep=0.04, fontproperties=dict(size=8))

# Adiciona o contorno dos estados e países.
ax.add_feature(estados, linewidth=0.5, edgecolor="k")

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex02.jpg', transparent=True, dpi=300, 
            bbox_inches='tight', pad_inches=0.1)