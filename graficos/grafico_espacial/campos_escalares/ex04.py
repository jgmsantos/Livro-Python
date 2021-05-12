import proplot as plot
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as crs
from cartopy.feature import NaturalEarthFeature
from cartopy.feature import ShapelyFeature
from cartopy.io.shapereader import Reader


# Abertura do arquivo NetCDF.
ds = xr.open_dataset('../../../dados/netcdf/Umidade.Solo.amazonia.2019.2020.nc', 
                     decode_times=False)

# Domínio espacial de interesse.
latN = 6
latS = -17
lonW = -75
lonE = -43

# Importação da variação e seleção do domínio espacial de interesse.
umidade_solo = ds.sel(lat=slice(latS, latN), lon=slice(lonW, lonE))

# Nome do shapefile do bioma de interesse.
shape_bioma = ShapelyFeature(Reader(f'../../../dados/shapefile/bioma_amazonia/states_amazon_biome.shp').geometries(), 
              crs.PlateCarree(), facecolor='none')

nlinhas = 3  # Linhas do painel.
ncolunas = 4  # Colunas do painel.
total_paineis = (nlinhas * ncolunas) + 1

fig, ax = plot.subplots(axheight=5, nrows=nlinhas, ncols=ncolunas, 
                        tight=True, proj='pcarree')

# Formatação do mapa.
ax.format(coast=False, borders=False, grid=False, 
          latlim=(latS, latN), lonlim=(lonW, lonE))

# Título da figura.
plt.suptitle('Percentil de Umidade do Solo: 2019', fontsize=35)

# Título de cada figura.
mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
       'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

# Valores de umidade do solo.
valores_de_umidade = [2, 5, 10, 20, 30, 70, 80, 90, 95, 98]

# Cores de interesse.
cores = ['dark maroon', 'blood', 'orange8', 'orange2', 'yellow', 
         'white', 'cyan', 'blue4', 'blue6', 'blue8', 
         'royal blue']

for i in range(1, total_paineis):

     # Plot da variável.
     map = ax[i-1].pcolormesh(umidade_solo['lon'], umidade_solo['lat'], 
                   umidade_solo['sfsm'][i-1, :, :],
                   cmap=cores, levels=valores_de_umidade, extend='both')

     # Insere o mês em cada figura.
     ax[i-1].set_title(mes[i-1], fontsize=30)
     # Adiciona o contorno do bioma de interesse.
     ax[i-1].add_feature(shape_bioma, linewidth=4., edgecolor='k')

#  Adiciona a barra de cores.
x = fig.colorbar(map, loc='b', width='4em', extendsize='12em', shrink=0.8, 
                 ticks=valores_de_umidade)
plt.tick_params(labelsize=30)  # Tamanho da fonte da barra de cores.
x.set_label('Percentil (%)', fontsize=30)  # Unidade da barra de cores.

# Salva a figura no formato ".jpg" com dpi=300.
fig.save('ex04.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)