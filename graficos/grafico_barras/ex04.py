import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Abertura do arquivo temperatura.txt com o separador TAB. Adiciona também o título de cada coluna.
# O arquivo tem formato de 12 linhas por 4 colunas. A primeira coluna é o mês, a segunda, a climatologia, 
# a terceria, o ano de 2019 e a quarta, o ano de 2020.
# Utiliza o separador '\t' que quer dizer TAB e cria o título para cada uma das colunas.
df = pd.read_csv('../../dados/texto/temperatura.txt', sep= '\t', names=['Mês', 'Climatologia', '2019', '2020'])

x = df['Mês']  # Importa os valores da coluna Mês.
y1 = df['Climatologia']  # Importa os valores da coluna Climatologia.
y2 = df['2020']  # Importa os valores da coluna 2020.

anomalia = y2 - y1  # Anomalia = desvio em relação a média (climatologia).

# Separa os valores mínimos e máximos.
above_threshold = np.maximum(anomalia - 0, 0)
below_threshold = np.minimum(anomalia, 0)

# Gera o plot com base nos limiares e separa o que é positivo (negativo) com vermelho (azul).
fig, ax = plt.subplots(figsize=(6,3))  # Largua e altura da figura.

ax.bar(x, above_threshold, 0.75, color="red")
ax.bar(x, below_threshold, 0.75, color="blue")

# Título principal da figura.
plt.title('Anomalia de Temperatura entre o ano 2020 e a Climatologia')

# Formatação do eixo x.
plt.xlabel('Mês', fontsize=10)  # Título do eixo x e o seu tamanho.
plt.xticks(fontsize=10)  # Tamanho dos rótulos do eixo x.
plt.xlim(0.5, 12.5)  # Define o mínimo e o máximo valor do eixo x.

# Formatação do eixo y.
plt.ylabel('Temperatura (ºC)', fontsize=10)  # Título do eixo y e o seu tamanho.
ax.set_ylim(-1.5, 1.5)  # Mínimo e máximo valor do eixo y.
ax.set_yticks(ticks=[-1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5])  # Rótulos do eixo y definido pelo usuário.
plt.yticks(fontsize=10)  # Tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

# Linha no valor zero, espessura = 0.5 e cor = black.
plt.axhline(linestyle='-', y=0, linewidth=0.5, color='black')

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex04.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)  