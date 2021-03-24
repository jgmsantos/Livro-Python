import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Leitura do arquivo no formato ".csv".
df1 = pd.read_csv('../dados/texto/eca_cdd.R.txt')
df1.set_index('Ano', inplace=True)  # Define a coluna "Ano" como o índice.

mes = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

med_mensal = []  # Cria uma lista vazia para armazenar os valores.

# Calcula a média mensal.
for coluna in mes:
    med_mensal.append(df1[coluna[:]].mean())

plt.bar(mes, med_mensal)

plt.show()

plt.close("all")

# Calcula o total anual.
total_anual = df1.sum(axis=1)
media = total_anual.mean()
pct_anual = list( ( (total_anual-media) / media ) * 100 )

x = np.arange(0, 18)

plt.bar(x, pct_anual)

plt.show()