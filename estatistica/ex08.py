import pandas as pd
from scipy import stats

# Abertura do arquivo utilizando o separador TAB e adiciona o título como primeira linha.
df = pd.read_csv('../dados/texto/variaveis_meteorologicas.txt', sep= '\t', 
                  names=['Data','UR','Temp','PREC','VelVento','DirVento'])

x = df['Temp']
y = df['PREC']

r = stats.spearmanr(x, y)

print(r)  # SpearmanrResult(correlation=0.677086961910298, pvalue=2.5283781966531542e-30)

