import pandas as pd
import matplotlib.pyplot as plt

# Abertura do arquivo temperatura.txt com o separador TAB. Adiciona também o título de cada coluna.
# O arquivo tem formato de 12 linhas por 4 colunas. A primeira coluna é o mês, a segunda, a climatologia, 
# a terceria, o ano de 2019 e a quarta, o ano de 2020.
# Utiliza o separador '\t' que quer dizer TAB e cria o título para cada uma das colunas.
df = pd.read_csv('../../dados/texto/temperatura.txt', sep= '\t', names=['Mês', 'Climatologia', '2019', '2020'])

x = df['Mês']  # Importa os valores da coluna Mês.
y1 = df['Climatologia']  # Importa os valores da coluna Climatologia.
y2 = df['2019']  # Importa os valores da coluna 2019.
y3 = df['2020']  # Importa os valores da coluna 2020.

fig, ax = plt.subplots()

# Título principal da figura.
plt.title('Climatologia de Temperatura')

# Formatação do eixo x.
plt.xlabel('Mês', fontsize=10)  # Título do eixo x e o seu tamanho.

# Formatação do eixo y.
plt.ylabel('Temperatura (ºC)', fontsize=10)  # Título do eixo y e o seu tamanho.
plt.ylim(25, 28)  # Mínimo e máximo valor do eixo y.
ax.set_yticks(ticks=[25, 25.5, 26, 26.5 , 27, 27.5, 28])  # Rótulos do eixo y definido pelo usuário.
plt.yticks(fontsize=10)  # Tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

# Plot da figura.
plt.scatter(x, y1, color='green', marker='o', label='Climatologia')
plt.scatter(x, y2, color='red', marker='o', label='2019')
plt.scatter(x, y3, color='blue', marker='o', label='2020')

#  Gera a legenda sem borda, define localização e o seu tamanho.
plt.legend(frameon =False, loc='lower left', fontsize=10)

#  Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex01.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)