import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
 
ax = plt.axes(projection=ccrs.PlateCarree())
 
# Adiciona os contornos estaduais, com resolução de 50m, a partir da base NaturalEarth (https://www.naturalearthdata.com/).
states_provinces = cfeature.NaturalEarthFeature(
                   category='cultural',
                   name='admin_1_states_provinces_lines',
                   scale='50m',
                   facecolor='none')
 
ax.add_feature(states_provinces, edgecolor='k')
 
ds['Wind_speed_gust_surface'].plot(ax=ax, cmap='bwr')