import matplotlib.pyplot as plt
import xarray as xr
import pandas as pd
import numpy as np
import cf_units
import datetime
import matplotlib as mpl

fig, ax = plt.subplots()

#  Abertura do arquivo com o xarray.
ds = xr.open_dataset('../../../dados/netcdf/PREC.IMERG.2020.amazonia.nc', decode_times=False)

prec = ds.sel(time='0').prec.plot()  # Seleciona um tempo em particular e visualiza a variável.

#  Título principal da figura.
plt.title('Precpipitação na Amazônia')

#  Formatação do eixo x:
plt.xlabel('Longitude')

#  Formatação do eixo y:
plt.ylabel('Latitude')

cbar = fig.colorbar(prec, orientation='horizontal')

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex01.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)