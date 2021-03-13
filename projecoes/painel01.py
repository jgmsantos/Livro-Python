import matplotlib.pyplot as plt
import cartopy.crs as ccrs

nlin = 3 

fig = plt.figure(figsize=(20, 10))

plt.subplots_adjust(wspace=-0.5, hspace=0.2)

ax = fig.add_subplot(nlin, 2, 1, projection=ccrs.PlateCarree())
ax.coastlines(resolution='110m')
ax.gridlines()
# Título principal da figura.
ax.set_title('PlateCarree(central_longitude=0.0)', fontsize=12, x=0.5, y=1)

ax = fig.add_subplot(nlin, 2, 2, projection=ccrs.PlateCarree(central_longitude=180))
ax.coastlines(resolution='110m')
ax.gridlines()
ax.set_title('PlateCarree(central_longitude=180.0)', fontsize=12, x=0.5, y=1)

ax = fig.add_subplot(nlin, 2, 3, projection=ccrs.AlbersEqualArea())
ax.coastlines(resolution='110m')
ax.gridlines()
ax.set_title('AlbersEqualArea', fontsize=12, x=0.5, y=1.0)

ax = fig.add_subplot(nlin, 2, 4, projection=ccrs.AzimuthalEquidistant(central_latitude=90))
ax.coastlines(resolution='110m')
ax.gridlines()
ax.set_title('AzimuthalEquidistant', fontsize=12, x=0.5, y=1)

ax = fig.add_subplot(nlin, 2, 5, projection=ccrs.EquidistantConic())
ax.coastlines(resolution='110m')
ax.gridlines()
ax.set_title('EquidistantConic', fontsize=12, x=0.5, y=1)

ax = fig.add_subplot(nlin, 2, 6, projection=ccrs.LambertConformal())
ax.coastlines(resolution='110m')
ax.gridlines()
ax.set_title('LambertConformal', fontsize=12, x=0.5, y=1)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('painel02.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)