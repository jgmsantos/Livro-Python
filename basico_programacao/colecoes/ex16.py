import pandas as pd
import numpy as np

# Dado mensal de precipitação.
df = pd.read_csv('../../dados/texto/pr.GPCP.txt', sep= '\t', names=['Ano', 'Mes', 'Prec'])

x = df.groupby('Mes')  # Agrupa por mês.

estatistica = x['Prec'].agg([np.size, np.sum, np.mean, np.std])

print(estatistica)