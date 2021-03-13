import matplotlib.pyplot as plt
import cartopy.crs as ccrs

ax = plt.axes(projection=ccrs.Robinson())
ax.coastlines(resolution='110m')
ax.gridlines()

# Título principal da figura.
plt.suptitle('Robinson', fontsize=10, y=0.81)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex15.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)