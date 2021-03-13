import matplotlib.pyplot as plt
import cartopy.crs as ccrs

nlin = 3 

fig = plt.figure(figsize=(20, 10))

plt.subplots_adjust(wspace=-0.5, hspace=0.2)

ax = fig.add_subplot(nlin, 2, 1, projection=ccrs.PlateCarree())
ax.coastlines(resolution='110m')
ax.gridlines()
ax.set_title('LambertCylindrical (central_longitude=0.0)', fontsize=12, x=0.5, y=1)

ax = fig.add_subplot(nlin, 2, 2, projection=ccrs.PlateCarree(central_longitude=180))
ax.coastlines(resolution='110m')
ax.gridlines()
ax.set_title('LambertCylindrical (central_longitude=180.0)', fontsize=12, x=0.5, y=1)

ax = fig.add_subplot(nlin, 2, 3, projection=ccrs.Mercator())
ax.coastlines(resolution='110m')
ax.gridlines()
ax.set_title('Mercator', fontsize=12, x=0.5, y=1)

ax = fig.add_subplot(nlin, 2, 4, projection=ccrs.Miller())
ax.coastlines(resolution='110m')
ax.gridlines()
ax.set_title('Miller (central_longitude=0.0)', fontsize=12, x=0.5, y=1)

ax = fig.add_subplot(nlin, 2, 5, projection=ccrs.Miller(central_longitude=180.0))
ax.coastlines(resolution='110m')
ax.gridlines()
ax.set_title('Miller (central_longitude=180.0)', fontsize=12, x=0.5, y=1)

ax = fig.add_subplot(nlin, 2, 6, projection=ccrs.Mollweide())
ax.coastlines(resolution='110m')
ax.gridlines()
ax.set_title('Mollweide', fontsize=12, x=0.5, y=1)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('painel02.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)