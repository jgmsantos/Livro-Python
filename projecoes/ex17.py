import matplotlib.pyplot as plt
import cartopy.crs as ccrs

ax = plt.axes(projection=ccrs.SouthPolarStereo())
ax.coastlines(resolution='110m')
ax.gridlines()

# Título principal da figura.
plt.suptitle('SouthPolarStereo', fontsize=10, y=0.95)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex17.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)