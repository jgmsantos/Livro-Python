import pandas as pd
import numpy as np

# Dado mensal de precipitação.
df = pd.read_csv('../../dados/texto/pr.GPCP.txt', sep= '\t', names=['Ano', 'Mes', 'Prec'])

#print(df)

x = df.groupby('Ano')  # Agrupa por ano.

# Calcula o acumulado anual para cada um dos anos.
acumulado_anual = x['Prec'].agg(np.sum)

print(acumulado_anual)