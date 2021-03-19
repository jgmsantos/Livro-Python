import pandas as pd
from scipy import stats

# Abertura do arquivo utilizando o separador TAB e adiciona o título como primeira linha.
df = pd.read_csv('../dados/texto/variaveis_meteorologicas.txt', sep= '\t', 
                  names=['Data','UR','Temp','PREC','VelVento','DirVento'])

x = df['PREC']  # Importa a precipitação desde 200301 a 202012 = 216 meses.

y = stats.describe(x)  # Calcula a estatística básica.

print(y)

# DescribeResult(nobs=216, minmax=(0.0, 458.3), mean=100.05740740740741, 
# variance=10534.8054332472, skewness=1.2779875424733596, kurtosis=1.2349900580132083)