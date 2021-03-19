import pandas as pd
from scipy import stats

# Abertura do arquivo utilizando o separador TAB e adiciona o título como primeira linha.
df = pd.read_csv('../dados/texto/variaveis_meteorologicas.txt', sep= '\t', 
                  names=['Data','UR','Temp','PREC','VelVento','DirVento'])

ur = df['UR']

x = stats.tmean(ur)
print(x)  # 74.32870370370371

# Exclui os valores igual e abaixo de 60% e igual e acima de 80%.
y = stats.tmean(ur, limits=(60, 80), inclusive=(False, False))  
print(y)  # 72.30075187969925

