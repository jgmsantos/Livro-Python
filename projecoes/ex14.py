import matplotlib.pyplot as plt
import cartopy.crs as ccrs

ax = plt.axes(projection=ccrs.Orthographic(central_longitude=180.0))
ax.coastlines(resolution='110m')
ax.gridlines()

# Título principal da figura.
plt.suptitle('Orthographic (central_longitude=180.0)', fontsize=10, y=0.93)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex14.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)