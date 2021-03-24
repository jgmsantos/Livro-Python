import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import accumulate

# Leitura do arquivo no formato ".csv".
df1 = pd.read_csv('../dados/texto/eca_cdd.R.txt')

df1.set_index('Ano', inplace=True)  # Define a coluna "Ano" como o índice.

mes = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

med_mensal = []  # Cria uma lista vazia para armazenar os valores.

# Calcula a média mensal (climatologia - jan, ..., dez).
for linha in mes:
    med_mensal.append(df1[linha[:]].mean())

plt.bar(mes, med_mensal)  # Gera o gráfico 1.

plt.savefig('ex01.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)

plt.show()  # Mostra o gráfico na tela.

plt.close("all")  # Limpa o ambiente gráfico para evitar erro com o próximo gráfico.

# Calcula para cada ano o total anual.
total_anual = df1.sum(axis=1)
# Calcula a média de todos os anos.
_mensal_cumulativo = total_anual.mean()
# Calcula o acréscimo ou decréscimo anual em porcentagem.
pct_anual = list(((total_anual-_mensal_cumulativo)/_mensal_cumulativo)*100)
# Calcula a anomalia.
anomalia_anual = list(total_anual-_mensal_cumulativo)

x = np.arange(0, 18)  # Gera um vetor com 18 posições (0 a 17 valores).

plt.bar(x, pct_anual)  # Gera o gráfico 2.

plt.savefig('ex02.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)

plt.show()  # Mostra o gráfico na tela.

plt.close("all")  # Limpa o ambiente gráfico para evitar erro com o próximo gráfico.

plt.bar(x, anomalia_anual)  # Gera o gráfico 3.

plt.savefig('ex03.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)

plt.show()  # Mostra o gráfico na tela.

plt.close("all")  # Limpa o ambiente gráfico para evitar erro com o próximo gráfico.

acumulado_anual = []  # Cria uma lista vazia para armazenar os valores.

# Calculando os valores cumulativos para cada ano.
for i in x:
     coluna = df1.iloc[i,:]
     acumulado_anual.append(list(accumulate(coluna)))

# Calcula a média mensal (climatologia) cumulativo de todos os anos.
media_mensal_cumulativo = np.average(acumulado_anual, axis=0)

plt.plot(mes, acumulado_anual[16], label='2019', color='r')  # Gera o gráfico 4.
plt.plot(mes, acumulado_anual[17], label='2020', color='b')  # Gera o gráfico 4.
plt.plot(mes, media_mensal_cumulativo, label='Média', color='y')  # Gera o gráfico 4.

# Gera a legenda sem borda, define localização e tamanho da fonte.
plt.legend(frameon =False, loc='lower right', fontsize=8)

plt.savefig('ex04.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)

plt.show()  # Mostra o gráfico na tela.