import pandas as pd
import matplotlib.pyplot as plt

# Abertura do arquivo temperatura.txt com o separador TAB. Adiciona 
# também o título de cada coluna. A primeira coluna é o mês, a segunda, 
# a climatologia, a terceira, o ano de 2019 e a quarta, o ano de 2020.
df = pd.read_csv('../../dados/texto/precipitacao.txt', 
                 sep= '\t', 
                 names=['Mês', 'Climatologia', '2019', '2020'])

x = df['Mês']  # Importa a coluna Mês.
y = df['Climatologia']  # Importa a coluna Climatologia.

fig, ax = plt.subplots(figsize=(7, 4))  # Largura e altura da figura.

# Gera o plot.
plt.bar(x, y, color='green', label='Precipitação', width=0.6, alpha=0.5) 

# Título principal da figura.
plt.title('Climatologia de precipitação', fontsize=8)

# Formatação do eixo x.
plt.xlabel('Mês', fontsize=8)  # Título do eixo x e o tamanho da fonte.
plt.xticks(fontsize=8)  # Tamanho dos rótulos do eixo x.

#  Formatação do eixo y.
plt.ylabel('Precipitação (mm/dia)', fontsize=8)
ax.set_ylim(0, 300)  #  Mínimo e máximo valor do eixo y.
# Rótulos do eixo y definido pelo usuário.
ax.set_yticks(ticks=[0, 50, 100, 150, 200, 250, 300])  
plt.yticks(fontsize=8)  #  Tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  #  Habilita o tickmark do eixo direito.

# Gera a legenda sem borda, define localização e o tamanho da fonte.
plt.legend(frameon =False, loc='upper right', fontsize=8)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex02.jpg', transparent=True, dpi=300, bbox_inches='tight', 
             pad_inches=0)