import pandas as pd
from scipy import stats

# Abertura do arquivo utilizando o separador TAB e adiciona o título como primeira linha.
df = pd.read_csv('../dados/texto/variaveis_meteorologicas.txt', sep= '\t', 
                  names=['Data','UR','Temp','PREC','VelVento','DirVento'])

ur = df['UR']

x = stats.tmean(ur)
print(x)  # 74.32870370370371

y = stats.tmean(ur, limits=(60, 80))  # Exclui os valores abaixo de 60% e acima de 80%.
print(y)  # 72.8407643312102