import pandas as pd
import matplotlib.pyplot as plt

# Abertura do arquivo temperatura.txt com o separador TAB. Adiciona também o título de cada coluna.
# O arquivo tem formato de 12 linhas por 4 colunas. A primeira coluna é o mês, a segunda, a climatologia, 
# a terceria, o ano de 2019 e a quarta, o ano de 2020.
df = pd.read_csv('../../dados/texto/temperatura.txt', sep= '\t', names=['Mês', 'Climatologia', '2019', '2020'])

x = df['Mês']  # Importa os valores da coluna Mês.
y1 = df['Climatologia']  # Importa os valores da coluna Climatologia.
y2 = df['2020']  # Importa os valores da coluna 2020.

anomalia = y2 - y1 # Anomalia = desvio em relação a média.

fig, ax = plt.subplots()

# Gera o plot
ax.plot(x, y1, x, y2, color='black')

# Preenche as curvas com veremlho e azul.
ax.fill_between(x, y1, y2, where=(y2 > y1), facecolor='red', alpha=0.5, label='Anomalia positiva (2020>clima)')
ax.fill_between(x, y1, y2, where=(y2 < y1), facecolor='blue', alpha=0.5, label='Anomalia negativa (2020<clima)')

# Título principal da figura.
plt.title('Diferença de Temperatura entre o ano 2020 e a Climatologia', fontsize=8)

# Formatação do eixo x.
plt.xlabel('Mês', fontsize=8)  # Título do eixo x e o tamanho da fonte.
plt.xticks(fontsize=8)  # Tamanho dos rótulos do eixo x.

# Formatação do eixo y.
plt.ylabel('Temperatura (ºC)', fontsize=8)  # Título do eixo y e o tamanho da fonte.
ax.set_ylim(25, 29)  # Mínimo e máximo valor do eixo y.
ax.set_yticks(ticks=[25, 25.5, 26, 26.5 , 27, 27.5, 28, 28.5, 29])  # Rótulos do eixo y definido pelo usuário.
plt.yticks(fontsize=8)  # Tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

# Gera a legenda sem borda, define localização e o tamanho da fonte.
plt.legend(frameon =False, loc='upper left', fontsize=8)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex05.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)