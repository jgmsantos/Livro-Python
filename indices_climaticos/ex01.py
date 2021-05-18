import xarray as xr
from climate_indices import indices


# Abertura do arquivo com o xarray.
ds = xr.open_dataset('../dados/netcdf/GPCP.nc')

# Importação da variável do arquivo.
prec = ds['precip']

# Agrupa a precipitação por lat/lon, ou seja, é criada uma série 
# temporal para cada ponto de lat/lon.
prec_agrupado = prec.stack(point=('lat', 'lon')).groupby('point')

scale = 3  # 1, 3, 6, 9, 12, 24, 48 meses.
distribution = indices.Distribution.pearson  # gamma ou pearson.
data_start_year = 1980  # Ano inicial.
calibration_year_initial = data_start_year  # Ano inicial.
calibration_year_final = 2015  # Ano final.
periodicity = periodicity = indices.compute.Periodicity.monthly

# Chama a função para calcular o SPI.
spi = xr.apply_ufunc(indices.spi,
                     prec_agrupado,
                     scale,
                     distribution,
                     data_start_year,
                     calibration_year_initial,
                     calibration_year_final,
                     periodicity)

# Função retorna o dado para o formato espacial (time, lat, lon).
spi = spi.unstack('point')  # <xarray.DataArray (time: 492, lat: 16, lon: 20)

# Altera o nome da variável para spi.
spi = spi.to_dataset(name='spi')

# 1) Dado espacial:
# Inserindo atributos.
spi.spi.attrs['long_name'] = f'Standardized Precipitation Index (SPI) - {scale} meses;'
spi.spi.attrs['units'] = 'Adimensional;'
spi.lat.attrs['units'] = 'degrees_north;'
spi.lon.attrs['units'] = 'degrees_east;'

# Opções de personalização do NetCDF.
encoding1={'spi': {'_FillValue': -999, 
                   'complevel': 9, 
                   'zlib': True},
           'time': {'zlib': False, '_FillValue': None},
           'lat': {'zlib': False, '_FillValue': None},
           'lon': {'zlib': False, '_FillValue': None}}

# Salva o resultado no NetCDF.
spi.to_netcdf(path='spi_espacial.nc', 
              unlimited_dims={'time':True}, 
              encoding=encoding1)

# 2) Série temporal:
# Média de todas as latitude e longitude gerando uma série temporal.
x = spi.mean(dim=('lon', 'lat'))  # time: 492

# Inserindo atributos.
x.spi.attrs['long_name'] = f'Standardized Precipitation Index (SPI) - {scale} meses;'
x.spi.attrs['units'] = 'Adimensional;'

# Opções de personalização do NetCDF.
encoding2={'spi': {'_FillValue': -999,
                   'complevel': 9,
                   'zlib': True},
                   'time': {'zlib': False,
                   '_FillValue': None}}

# Salva o resultado no NetCDF.
x.to_netcdf(path='spi_serie.nc', 
            unlimited_dims={'time':True}, 
            encoding=encoding2)