import pandas as pd
from scipy import stats

# Abertura do arquivo utilizando o separador TAB e adiciona o título como primeira linha.
df = pd.read_csv('../dados/texto/variaveis_meteorologicas.txt', sep= '\t', 
                  names=['Data','UR','Temp','PREC','VelVento','DirVento'])

x = df['Temp']
y = df['PREC']

r = stats.pearsonr(x, y)

          #          r                  p-value
print(r)  # (0.5522538017058155, 1.2107247393256543e-18)

