import matplotlib.pyplot as plt
import cartopy.crs as ccrs

ax = plt.axes(projection=ccrs.EquidistantConic())
ax.coastlines(resolution='110m')
ax.gridlines()

# Título principal da figura.
plt.suptitle('EquidistantConic)', fontsize=10, y=0.8)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex05.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)