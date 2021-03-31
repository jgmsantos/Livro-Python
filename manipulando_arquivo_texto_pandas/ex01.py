import pandas as pd

# Leitura do arquivo no formato ".csv".
df1 = pd.read_csv('../dados/texto/eca_cdd.R.txt')

#print(df1.head())  # Imprime as 5 primeiras linhas de cada coluna.
#
#print(df1.tail())  # Imprime as últimas 5 linhas de cada coluna.
#
#print(df1.shape)  # 18 linhas x 13 colunas
#
#print(type(df1))  # <class 'pandas.core.frame.DataFrame'>
#
#print(df1.index)  # RangeIndex(start=0, stop=18, step=1)
#
#print(df1.describe())  # Apresenta uma estatística sobre os dados.
#
#print(df1.columns)  # Imprime o título das colunas.
#
#print(df1.isnull())  # Checa se tem dado ausente em alguma coluna.
#
#print(df1.isnull().sum())  # Soma o total de valores nulos em casa coluna.
#
#print(df1.dropna(how='any'))  # Deleta a linha na caso de valores faltantes.
#
#print(df1.dropna(how='all'))  # Deleta a linha caso todos os valores sejam faltantes.
#
## Deleta a linha caso os meses Fev ou Jul tenham valores faltantes.
#print(df1.dropna(subset=['Fev', 'Jul'], how='any'))
#
## Deleta a linha caso os meses Fev e Jul tenham valores faltantes.
#print(df1.dropna(subset=['Fev', 'Jul'], how='all'))  
#
## Abertura do arquivo.
#df2 = pd.read_csv('../dados/texto/direcao_vento.txt')
#
## Realiza o agrupamento dos valores e sua contagem. Não considera valores faltantes.
#print(df2['Direção'].value_counts())

# Realiza o agrupamento dos valores e sua contagem. Considera valores faltantes (dropna=False).
#print(df2['Direção'].value_counts(dropna=False))

# Retorna informações sobre o arquivo.
#print(df1.info())

# Deletar uma coluna. Neste caso foi removida a coluna Ano.
#df1.drop(['Ano'], axis=1, inplace=True)
#print(df1.info())

# Retorna o meno e o maior valor do conjunto de dados. Neste exemplo serão retornado os 4 menores e maiores valores da coluna Jan, respectivamente.
#print(df1.nsmallest(4, 'Jan'))
#print(df1.nlargest(4, 'Jan'))

#df1.clear()

# Seleciona linhas específicas por meio das colunas. Retorna os 6 primeiros valores das colunas Jan e Fev.
#x = df1.loc[:5,['Jan', 'Fev']]
#print(x)

# Seleciona linhas específicas de acordo com a sua posição especifica por linhas e colunas. Retorna os 6 primeiros valores das colunas Jan e Fev.
#x = df1.iloc[:3,:3]
#print(x)

# Seleciona valores por intervalo de interesse. Seleciona os valores de Jul maiores que 15 e menores que 25.
#x = df1.query('15 < Jul < 25').head()
#print(x)

# Definir a coluna como index. Definindo a coluna Ano como index.
#print(df1.set_index('Ano').head(4))

# Definir a coluna como index. Definindo a coluna Ano como index.
x = df1.set_index('Ano').head(4)

print(x['Ano'].sort_value(by='Ano'))