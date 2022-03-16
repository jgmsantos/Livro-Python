import xarray as xr
import proplot as plot
import numpy as np
from esmtools.stats import corr
 
 
# Ignora mensagem de aviso pois no cálculo da correlação 
# são encontrados valores UNDEF.
np.seterr(divide='ignore', invalid='ignore')
 
# Define o tamanho da fonte do título, rótulos e títulos dos eixos x e y.
plot.rc.fontsize = 10  
 
# Abertura do arquivo.
sst = xr.open_dataset('../../../dados/netcdf/sst.1981.2010.nc')
 
# Cálculo da anomalia (valor observado - média).
asst = sst.groupby('time.month') - sst.groupby('time.month').mean('time')
 
# Anomalia de SST na região do Niño 3.4
nino34 = asst.sel(lon=slice(190, 240), lat=slice(5, -5)).mean(("lon", "lat"))
 
fig, ax = plot.subplots(figsize=(8, 4))
 
# Plota da série temporal da SST na região do Niño 3.4.
ax.bar(np.array(nino34['time']), np.array(nino34['sst']), negpos=True)
 
ax.format(ylabel='Anomalia de SST ($\degree$C)',
          title='Anomalia de SST na região do Niño 3.4', 
          ylim=(-3, 3), 
          yminorlocator=0.5, 
          ylocator=np.arange(-3, 3.5, 0.5), 
          yformatter='{x:.1f}', 
          xlim=(np.datetime64('1981-01-01'), np.datetime64('2010-12-01')),
          xlocator='year', 
          xminorlocator='year', 
          xformatter='%b%Y')
 
ax.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.
 
# Adiciona linha no valor 0.5C no eixo y que define o evento El Niño.
ax.axhline(0.5, color='red', linestyle='--')
 
# Adiciona linha no valor -0.5C no eixo y que define o evento La Niña.
ax.axhline(-0.5, color='blue', linestyle='--')
 
# Correlação entre a Anomalia de SST e a anomalia na região do Niño 3.4.
corr_asst_nino34 = corr(asst['sst'], nino34['sst'], dim='time')
 
fig1, ax1 = plot.subplots(axwidth=5, tight=True,
                          proj='ortho', proj_kw={'lon_0': 220})
 
# Formatação do mapa.
ax1.format(coast=True, borders=True, innerborders=False,
          labels=False, latlines=10, lonlines=10,
          facecolor='gray',
          title='Correlação entre as anomalias de SST e do Niño 3.4')
 
# Plota da figura.
map1 = ax1.contourf(asst['lon'], asst['lat'], corr_asst_nino34,
                   levels=plot.arange(-1.0, 1.0, 0.2), cmap='RdBu_r')
 
# Adicona a barra de cores.
fig1.colorbar(map1, loc='b', label='Correlação de Pearson')
 
# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
fig1.savefig('ex01.jpg', 
              transparent=True, 
              dpi=300, 
              bbox_inches='tight', 
              pad_inches=0)