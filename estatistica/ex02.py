import pandas as pd
from scipy import stats

# Abertura do arquivo utilizando o separador TAB e adiciona o título como primeira linha.
df = pd.read_csv('../dados/texto/variaveis_meteorologicas.txt', sep= '\t', 
                  names=['Data','UR','Temp','PREC','VelVento','DirVento'])

ur = df['UR']
temp = df['Temp']
prec = df['PREC']
vel = df['VelVento']
dir = df['DirVento']

lista_variaveis = [ur, temp, prec, vel, dir]

[print("Resultado: ", stats.describe(variavel)) for variavel in lista_variaveis]

