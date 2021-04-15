import proplot as plot
import xarray as xr

fig, ax = plot.subplots(axheight=5, tight=True,
                         proj='pcarree',)

# Abertura do arquivo com o xarray.
ds = xr.open_dataset('../../../dados/netcdf/tmed.clima.amazonia.nc', decode_times=False)

tmed = ds.tmed[0,:,:]

ax.format(coast=True, borders=True, innerborders=False,
          labels=True, latlines=5, lonlines=5,
          latlim=(5.75, -17.75), lonlim=(-75, -43),
          title='Temperatura no bioma Amazônia')

ax.set_ylabel('Latitude', fontsize=7)  # Define o tamanho do título do eixo y.
ax.set_xlabel('Latitude', fontsize=7)  # Define o tamanho do título do eixo y.

map = ax.contourf(ds['lon'], ds['lat'],
                   tmed,
                   cmap='coolwarm', levels=plot.arange(25, 29, 0.5),
                   extend='both')

fig.colorbar(map, loc='b', label='Temperatura ($\degree$C)', orientation='horizontal')

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
fig.save('ex04.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)