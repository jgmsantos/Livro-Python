import pandas as pd

# Leitura do arquivo no formato ".csv".
df1 = pd.read_csv('../dados/texto/eca_cdd.R.txt')

print(df1.head())  # Imprime as 5 primeiras linhas de cada coluna.

print(df1.tail())  # Imprime as últimas 5 linhas de cada coluna.

print(df1.shape)  # 18 linhas x 13 colunas

print(type(df1))  # <class 'pandas.core.frame.DataFrame'>

print(df1.index)  # RangeIndex(start=0, stop=18, step=1)

print(df1.describe())  # Apresenta uma estatística sobre os dados.

print(df1.columns)  # Imprime o título das colunas.

print(df1.isnull())  # Checa se tem dado ausente em alguma coluna.

print(df1.isnull().sum())  # Soma o total de valores nulos em casa coluna.

print(df1.dropna(how='any'))  # Deleta a linha na caso de valores faltantes.

print(df1.dropna(how='all'))  # Deleta a linha caso todos os valores sejam faltantes.

# Deleta a linha caso os meses Fev ou Jul tenham valores faltantes.
print(df1.dropna(subset=['Fev', 'Jul'], how='any'))

# Deleta a linha caso os meses Fev e Jul tenham valores faltantes.
print(df1.dropna(subset=['Fev', 'Jul'], how='all'))  

# Abertura do arquivo.
df2 = pd.read_csv('../dados/texto/direcao_vento.txt')

# Realiza o agrupamento dos valores e sua contagem. Não considera valores faltantes.
print(df2['Direção'].value_counts())

# Realiza o agrupamento dos valores e sua contagem. Considera valores faltantes (dropna=False).
print(df2['Direção'].value_counts(dropna=False))