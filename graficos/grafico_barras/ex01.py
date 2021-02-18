import pandas as pd
import matplotlib.pyplot as plt

#  Abertura do arquivo temperatura.txt com o separador TAB. Adiciona também o título de cada coluna.
#  O arquivo tem formato de 12 linhas por 4 colunas. A primeira coluna é o mês, a segunda, a climatologia, 
#  a terceria, o ano de 2019 e a quarta, o ano de 2020.
#  Utiliza o separador '\t' que quer dizer TAB e cria o título para cada uma das colunas.
df = pd.read_csv('../../dados/texto/precipitacao.txt', sep= '\t', names=['Mês', 'Climatologia', '2019', '2020'])

x = df['Mês']  #  Importa a coluna Mês.
y = df['Climatologia'] #  Importa a coluna Climatologia.

#  Gera o plot.
plt.bar(x, y) 

#  Mostra na tela o resultado.
plt.show()  