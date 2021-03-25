import pandas as pd
import numpy as np

# Dado mensal de precipitação.
df = pd.read_csv('../../dados/texto/pr.GPCP.txt', sep= '\t', names=['Ano', 'Mes', 'Prec'])

x = df.groupby('Mes')  # Agrupa por mês.

# Calcula a média mensal (climatologia). O cálculo considera a média de 
# todos os jan, fev, ..., dez. O resultado final será um arquivo com 12 meses.
media_mensal = x['Prec'].agg(np.mean)

# Conta o total de meses para cada mês.
total_meses = x['Prec'].agg(np.size)

print(media_mensal)

print(total_meses)