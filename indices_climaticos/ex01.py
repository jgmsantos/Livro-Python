import xarray as xr
from climate_indices import indices
import matplotlib.pyplot as plt

# Abertura do arquivo com o xarray.
ds = xr.open_dataset('../dados/netcdf/GPCP.nc')

# Importação da variável do arquivo.
prec = ds['precip']

# Agrupa a precipitação por lat/lon, ou seja, é criada uma série 
# temporal para cada ponto de lat/lon.
prec_agrupado = prec.stack(point=('lat', 'lon')).groupby('point')

scale = 3  # 3, 6, 9, 12 meses.
distribution = indices.Distribution.pearson  # gamma ou pearson.
data_start_year = 2010  # Ano inicial.
calibration_year_initial = 2010  # Ano inicial.
calibration_year_final = 2015  # Ano final.
periodicity = periodicity = indices.compute.Periodicity.monthly  # monthly ou daily.

# Chama a função.
spi = xr.apply_ufunc(indices.spi,
                        prec_agrupado,
                        scale,
                        distribution,
                        data_start_year,
                        calibration_year_initial,
                        calibration_year_final,
                        periodicity)

# Função para que o dado retorne para o formato espacial.
spi = spi.unstack('point')

# Média de todas as latitude e longitude gerando uma série temporal.
spi.mean(dim=('lon', 'lat')).plot()

plt.show()