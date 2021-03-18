import pandas as pd
import matplotlib.pyplot as plt

# Abertura do arquivo temperatura.txt com o separador TAB. Adiciona também o título de cada coluna.
# O arquivo tem formato de 12 linhas por 4 colunas. A primeira coluna é o mês, a segunda, a climatologia, 
# a terceria, o ano de 2019 e a quarta, o ano de 2020.
df = pd.read_csv('../../dados/texto/temperatura.txt', sep= '\t', names=['Mês', 'Climatologia', '2019', '2020'])

x = df['Mês']  # Importa a coluna Mês.
y = df['Climatologia']  # Importa a coluna Climatologia.

# Gera o plot.
plt.plot(x, y) 

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex01.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)