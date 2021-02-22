import pandas as pd
import matplotlib.pyplot as plt

# Abertura do arquivo temperatura.txt com o separador TAB. Adiciona também o título de cada coluna.
# O arquivo tem formato de 12 linhas por 4 colunas. A primeira coluna é o mês, a segunda, a climatologia, 
# a terceria, o ano de 2019 e a quarta, o ano de 2020.
# Utiliza o separador '\t' que quer dizer TAB e cria o título para cada uma das colunas.
df = pd.read_csv('../../dados/texto/precipitacao.txt', sep= '\t', names=['Mês', 'Climatologia', '2019', '2020'])

x = df['Mês']  # Importa a coluna Mês.
y = df['Climatologia']  # Importa a coluna Climatologia.

# Comprimento e altura da figura.
fig, ax = plt.subplots(figsize=(7, 4))

# Gera o plot.
plt.bar(x, y, color='green', label='Precipitação', width=0.6) 

# Título principal da figura.
plt.title('Climatologia de precipitação')

# Formatação do eixo x.
plt.xlabel('Mês', fontsize=10)  # Título do eixo x e o seu tamanho.
plt.xticks(fontsize=10)  # Tamanho dos rótulos do eixo x.

#  Formatação do eixo y.
plt.ylabel('Precipitação (mm/dia)', fontsize=10)  #  Título do eixo y e o seu tamanho.
ax.set_ylim(0, 300)  #  Mínimo e máximo valor do eixo y.
ax.set_yticks(ticks=[0, 50, 100, 150, 200, 250, 300])  #  Rótulos do eixo y definido pelo usuário.
plt.yticks(fontsize=10)  #  Tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  #  Habilita o tickmark do eixo direito.

#   Gera a legenda sem borda, define localização e o seu tamanho.
plt.legend(frameon =False, loc='upper right', fontsize=10)

#   Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex02.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)

#  Mostra na tela o resultado.
plt.show()  