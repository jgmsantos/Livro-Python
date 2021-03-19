import pandas as pd
from scipy import stats

# Abertura do arquivo utilizando o separador TAB e adiciona o título como primeira linha.
df = pd.read_csv('../dados/texto/variaveis_meteorologicas.txt', sep= '\t', 
                  names=['Data','UR','Temp','PREC','VelVento','DirVento'])

dir = df['DirVento']

y = stats.mode(dir)

print(y)  # ModeResult(mode=array([74]), count=array([15]))

# O valor 74 é o que mais se repete. Foram 15 repetições.