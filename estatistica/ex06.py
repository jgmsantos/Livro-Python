import pandas as pd
from scipy import stats

# Abertura do arquivo utilizando o separador TAB e adiciona o título como primeira linha.
df = pd.read_csv('../dados/texto/variaveis_meteorologicas.txt', sep= '\t', 
                  names=['Data','UR','Temp','PREC','VelVento','DirVento'])

ur = df['UR']

x = stats.tmin(ur)
print(x)  # 56

# Retorna o valor mínimo dado um limite inferior.
y = stats.tmin(ur, lowerlimit=70)
print(y)  # 70

# Retorna o valor mínimo dado um limite inferior sendo que ele é excluído.
z = stats.tmin(ur, lowerlimit=70, inclusive=False)
print(z)  # 71

