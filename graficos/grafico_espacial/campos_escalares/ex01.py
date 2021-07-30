import proplot as plot
import xarray as xr
from cartopy.feature import NaturalEarthFeature


# Abertura do arquivo NetCDF.
ds = xr.open_dataset('../../../dados/netcdf/Umidade.Solo.amazonia.2019.2020.nc', 
                     decode_times=False)

#print(ds)  # Informações sobre o arquivo.

# Valores de umidade do solo.
valores_de_umidade = [2, 5, 10, 20, 30, 70, 80, 90, 95, 98]  # 10 cores.

# Cores de interesse. Sempre número de cores + 1, ou seja, 10 + 1 = 11 cores.
cores = ['dark maroon', 'blood', 'orange8', 'orange2', 'yellow', 'white', 
         'cyan', 'blue4', 'blue6', 'blue8', 'royal blue']

# Definição da área de interesse.
variavel = ds.sel(lat=slice(-17, 6), lon=slice(-75, -43))

# Linhas do continente.
# O admin_1_states_provinces_shp é um arquivo do Python.
estados = NaturalEarthFeature(category="cultural", scale="50m", 
          facecolor="none", name="admin_1_states_provinces_shp")

fig, ax = plot.subplots(tight=True, proj='pcarree',)

# Formatação do mapa.
ax.format(coast=False, borders=False, innerborders=False,
          labels=True, grid=True, latlines=5, lonlines=5,
          latlim=(-17, 6), lonlim=(-75, -43),
          small='8px', large='11px',
          title='Percentil de Umidade do Solo')

# Plot da variável. Nome da variável do arquivo: "sfsm".
map = ax.pcolormesh(variavel['lon'], variavel['lat'], 
                   variavel['sfsm'][0, :, :], cmap=cores, 
                   levels=valores_de_umidade, extend='both')

# Adiciona o contorno dos estados e países.
ax.add_feature(estados, linewidth=1, edgecolor="k")

#  Adiciona a barra de cores.
x = fig.colorbar(map, loc='b', width='12px', shrink=0.95, 
                 label='Percentil (%)', labelsize=5, 
                 ticklabelsize=5, ticks=valores_de_umidade)

# Salva a figura no formato ".jpg" com dpi=300.
fig.save('ex01.jpg', transparent=True, dpi=300, 
          bbox_inches='tight', pad_inches=0.02)