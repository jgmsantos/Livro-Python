import xarray as xr
import proplot as pplt
import cartopy.crs as crs
import salem
from cartopy.feature import ShapelyFeature
from cartopy.io.shapereader import Reader
 
# Abertura do arquivo NetCDF.
ds = xr.open_dataset('../dados/netcdf/MERGE_CPTEC_20220131.nc')
 
# Abertura do arquivo shapefile. O arquivo "states_amazonia_biome.shp" será
# utilizado para mascarar os dados.
shp = salem.read_shapefile('../dados/shapefile/bioma_amazonia/states_amazon_biome.shp')
 
#print(shp)  # Visualiza as informações do shapefile.
 
# Os nomes 'NORTE', 'NORDESTE' e 'CENTRO-OESTE' vieram do comando "print(shp)".
 
# As regiões a serem utilizadas para mascarar o dado.
shp_amazonia = shp.loc[(shp['NM_REGIAO'] == 'NORTE') |
                       (shp['NM_REGIAO'] == 'NORDESTE') |
                       (shp['NM_REGIAO'] == 'CENTRO-OESTE')]
 
fig, ax = pplt.subplots(proj='pcarree')
 
# Formatação do mapa.
ax.format(coast=False, borders=False, grid=False,
          latlim=(-17, 6),
          lonlim=(-74, -43),
          linewidth=0)
 
# Na linha abaixo o trecho "salem.roi(shape=shp_amazonia)" é
# responsável por aplicar a máscara no dado, isto é, mascara 
# o dado apenas no domínio do Bioma Amazônia. A variável a 
# ser utilizada para manipulação futura ou plot é a "prec_mask".
prec_mask = ds.prec.salem.roi(shape=shp_amazonia)

# Plot da figura. Plota apenas o primeiro tempo.
ax.pcolormesh(ds.longitude,
              ds.latitude,
              prec_mask[0,:,:],
              cmap='Crest')
 
# Nome do arquivo shapefile que será utilizado para desenhar o contorno no mapa.
shape_amazonia = ShapelyFeature(
                 Reader('../dados/shapefile/bioma_amazonia/states_amazon_biome.shp').geometries(),
                 crs.PlateCarree(), facecolor='none'
                 )
 
# Adiciona o contorno do shapefile ao mapa de precipitação.
ax.add_feature(shape_amazonia, linewidth=1, edgecolor='black')
 
# Salva a figura.
fig.save('ex01.jpg', transparent=True, dpi=300, bbox_inches='tight',
          pad_inches=0.1)