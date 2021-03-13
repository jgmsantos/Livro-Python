import matplotlib.pyplot as plt
import cartopy.crs as ccrs

ax = plt.axes(projection=ccrs.Miller())
ax.coastlines(resolution='110m')
ax.gridlines()

# Título principal da figura.
plt.suptitle('Miller (central_longitude=0.0)', fontsize=10, y=0.93)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex10.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)