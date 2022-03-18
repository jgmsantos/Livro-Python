from siphon.catalog import TDSCatalog
from siphon.ncss import NCSS
import numpy as np
from datetime import datetime, timedelta
import xarray as xr
import os


def get_gfs(year, month, day, fcst_hr, cycle):
  '''
    Função que faz o download de previsões do modelo GFS de modo personalizado, definindo hora, data, área e variáveis.
    Vale ressaltar que em horário de análises (i.e. f000) possuem 93 variáveis, enquanto as previsões (i.e. f003 em diante) 
    possuem 138 variaveis

    Informações de entrada da função:
 
    year    : ano de inicio da previsão
    month   : mes de inicio da previsão
    day     : dia de inicio da previsão
    fcst_hr : Hora de previsão (003, 006, ...)
    cycle   : ciclo de inicialização, 00, 06, 12 ou 18 UTC
    
  '''
  
  dtime = f"{year}{str(month).zfill(2)}{str(day).zfill(2)}"
  fname = f"{year}{str(month).zfill(2)}{str(day).zfill(2)}{str(cycle).zfill(2)}.f{str(fcst_hr).zfill(3)}"
 
  # Criando URL para consulta do catálogo de dados GFS.
  catUrl = f"https://rda.ucar.edu/thredds/catalog/files/g/ds084.1/{year}/{dtime}/catalog.xml";
  datasetName = f"gfs.0p25.{fname}.grib2";
 
  # Catálogo completo de dados disponíveis no servidor THREDDS do RDA/UCAR: https://rda.ucar.edu/thredds/catalog/catalog.html
  catalog = TDSCatalog(catUrl) 
  ds = catalog.datasets[datasetName]
 
  # Criando objeto de seleção personalizada do dado.
  ncss = ds.subset() 
  
  # Criando instância da classe de consulta.
  query = ncss.query()
 
  # Download em uma área específica
  query.lonlat_box(east=-40, west=-50, south=-20, north=-10) 
 
  # Download em apenas um ponto (Exemplo, estações INMET de Salvador-BA).
  # query.lonlat_point(lon=-38.5166, lat=-13.0166)
 
  # Definindo a data de download, a partir de 2015 ().
  query.time( datetime(year, month, day, cycle) + timedelta(hours=fcst_hr) )
 
  # Seleção de variáveis (Se desejar, use 'print(ncss.variables)' para ver a lista completa).
  query.variables(    
    'Temperature_surface',
    'u-component_of_wind_height_above_ground',
    'v-component_of_wind_height_above_ground',    
    'Wind_speed_gust_surface',
    ).add_lonlat()  
  # query.variables('all') # Caso queira todas variáveis disponíveis.
 
  # Definindo o formato.
  query.accept('netcdf4')
 
  # Fazendo solicitação no servidor THREDDS do RDA/UCAR a partir das consultas acima.
  nc = ncss.get_data(query)
 
  # Convertendo o arquivo obtido para XArray e salvando em NetCDF.
  dataset = xr.open_dataset(xr.backends.NetCDF4DataStore(nc))
  dataset.to_netcdf(f"{ds.name[:-6]}.nc")
  return dataset
 
# Coletando hora/data para calcular tempo de execução do código.
stime_run = datetime.now() 
yr = 2018       ## Ano
mm = 2          ## Mês
day = 20        ## Dia
cycle = 0       ## Ciclo de assimilação
fcst_hr = 36    ## Hora da previsão
 
## Obtendo data/hora antes da função get_gfs para mensurar tempo de execução final.
stime = datetime(yr,mm,day,cycle)

valid = stime + timedelta(hours=int(fcst_hr))

## Chamando a função get_gfs para baixar previsões a partir da data/hora definida acima.
ds = get_gfs(yr,mm,day,fcst_hr,cycle)

print(f"Download do GFS 0.25p || Data/Hora de inicialização: {stime} | Data/Hora válida: {valid} (fcst_hr={str(fcst_hr).zfill(3)}; cycle={str(cycle).zfill(2)})")
print("\nTempo total de execução do script: ", datetime.now() - stime_run) 
