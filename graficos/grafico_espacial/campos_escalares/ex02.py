import proplot as plot
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as crs
from cartopy.feature import ShapelyFeature
from cartopy.io.shapereader import Reader


# Abertura do arquivo NetCDF.
ds = xr.open_dataset('../../../dados/netcdf/Umidade.Solo.amazonia.2019.2020.nc', decode_times=False)

#print(ds)  # Informações sobre o arquivo.

# Valores de umidade do solo.
valores_de_umidade = [2, 5, 10, 20, 30, 70, 80, 90, 95, 98]  # 10 cores.

# Cores de interesse. Sempre número de cores + 1, ou seja, 10 + 1 = 11 cores.
cores = ['dark maroon', 'blood', 'orange8', 'orange2', 'yellow', 'white', 
          'cyan', 'blue4', 'blue6', 'blue8', 'royal blue']

# Importação da variável.
umidade_solo = ds.sel(lat=slice(-17, 6), lon=slice(-75, -43))

# Linhas do continente.
# Nome do shapefile do bioma de interesse.
bioma = ShapelyFeature(Reader(f'../../../dados/shapefile/bioma_amazonia/states_amazon_biome.shp').geometries(), 
        crs.PlateCarree(), facecolor='none')

fig, ax = plot.subplots(figsize=(7, 4), tight=True, proj='pcarree',)

# Formatação do mapa.
ax.format(coast=False, borders=False, innerborders=False,
          labels=True, grid=True, latlines=5, lonlines=5,
          latlim=(-17, 6), lonlim=(-75, -43),
          title='Percentil de Umidade do Solo')

# Plot da variável.
map = ax.pcolormesh(umidade_solo['lon'], umidade_solo['lat'], 
                   umidade_solo['sfsm'][0, :, :], cmap=cores, 
                   levels=valores_de_umidade, extend='both')

# Adiciona o contorno dos estados e países.
ax.add_feature(bioma, linewidth=1, edgecolor="k")

#  Adiciona a barra de cores.
x = fig.colorbar(map, loc='b', width='1.5em', extendsize='2em', 
                 shrink=0.57, ticks=valores_de_umidade)
plt.tick_params(labelsize=8)  # Tamanho da fonte da barra de cores.
x.set_label('Percentil (%)', fontsize=8)  # Unidade da barra de cores.

# Salva a figura no formato ".jpg" com dpi=300.
fig.save('ex02.jpg', transparent=True, dpi=300)