import pandas as pd
import matplotlib.pyplot as plt

# Abertura do arquivo temperatura.txt com o separador TAB. Adiciona também o título de cada coluna.
# O arquivo tem formato de 12 linhas por 4 colunas. A primeira coluna é o mês, a segunda, a climatologia, 
# a terceria, o ano de 2019 e a quarta, o ano de 2020.
# Utiliza o separador '\t' que quer dizer TAB e cria o título para cada uma das colunas.
df = pd.read_csv('../../dados/texto/temperatura.txt', sep= '\t', names=['Mês', 'Climatologia', '2019', '2020'])

x = df['Mês']  # Importa os valores da coluna Mês.
y = df['Climatologia'] # Importa os valores da coluna Climatologia.

# Gera o plot.
plt.plot(x, y, color='green', marker='o', linestyle='solid', linewidth=10, markersize=10, alpha=150)  

# Mostra na tela o resultado.
plt.show()  