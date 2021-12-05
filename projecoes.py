import proplot as plot

# Table of basemap projections
#projs = ['cyl', 'merc', 'sinu', 'robin', 'moll', 'hammer']
#projs_string = ['Cylindrical Equidistant (cyl)', 'Mercator (merc)', 
#                'Sinusoidal (sinu)', 'Robinson (robin)', 
#                'Mollweide (moll)', 'Hammer (hammer)']

projs = ['geos', 'ortho', 'nsper', 'stere', 'spstere', 'npstere']
projs_string = ['Geostationary (geos)', 'Orthographic (ortho)', 
                'Near-Sided Perspective (nsper)', 'Stereographic (stere)', 
                'South-Polar Stereographic (spstere)', 'North-Polar Stereographic (npstere)']

fig, ax = plot.subplots(ncols=2, nrows=3, proj='npstere', proj_kw={'lon_0': -120})

for proj, ax in zip(projs_string, ax):
    ax.format(land=True, title=proj, labels=False, large='20px')

# Salva a figura no formato ".jpg" com dpi=300.
fig.save('projecao02.jpg', transparent=True, dpi=300, 
         bbox_inches='tight', pad_inches=0.02)