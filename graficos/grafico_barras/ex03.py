import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#  Abertura do arquivo temperatura.txt com o separador TAB. Adiciona também o título de cada coluna.
#  O arquivo tem formato de 12 linhas por 4 colunas. A primeira coluna é o mês, a segunda, a climatologia, 
#  a terceria, o ano de 2019 e a quarta, o ano de 2020.
#  Utiliza o separador '\t' que quer dizer TAB e cria o título para cada uma das colunas.
df = pd.read_csv('../../dados/texto/precipitacao.txt', sep= '\t', names=['Mês', 'Climatologia', '2019', '2020'])

x = df['Mês']  #  Importa os valores da coluna Mês.
y1 = df['Climatologia']  #  Importa os valores da coluna Climatologia.
y2 = df['2019']  #  Importa os valores da coluna 2019.
y3 = df['2020']  #  Importa os valores da coluna 2020.

#  Comprimento e altura da figura.
plt.figure(figsize=(8, 4))

#  Posição onde serão geradas as barras.
x1 = np.arange(len(y1))  #  [ 0  1  2  3  4  5  6  7  8  9 10 11 12]. Vetor com os índices.
x2 = [y + 0.25 for y in x1]  #  [0.25, 1.25, 2.25, 3.25, 4.25, 5.25, 6.25, 7.25, 8.25, 9.25, 10.25, 11.25, 12.25]. Valores do eixo x para desenhar a primeira barra.
x3 = [y + 0.25 for y in x2]  #  [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5]. Valores do eixo x para desenhar a segunda barra.

#  Plot da figura. color = cor da barra, width = largura da barra, label = nome que vai aparecer na legeda e 
#  alpha = aplica efeito de transparência na barra.
plt.bar(x1, y1, color='green', width=0.25, label='Climatologia', alpha=0.30)
plt.bar(x2, y2, color='red', width=0.25, label='2019', alpha=0.30)
plt.bar(x3, y3, color='blue', width=0.25, label='2020', alpha=0.30)

#  Título principal da figura.
plt.title('Precipitação no bioma Amazônia')

#  Formatação do eixo x.
plt.xlabel('Mês', fontsize=10)  #  Título do eixo x e o seu tamanho.
plt.xticks([r + 0.25 for r in range(len(y1))], x, fontsize=10)  #  Tamanho dos rótulos do eixo x.
plt.xlim(0.5, 13)  #  Mínimo e máximo valor do eixo x.

#  Formatação do eixo y.
plt.ylabel('Precipitação (mm/dia)', fontsize=10)  #  Título do eixo y e o seu tamanho.
plt.ylim(0, 300)  #  Mínimo e máximo valor do eixo y.
plt.yticks(ticks=[0, 50, 100, 150, 200, 250, 300])  #  Rótulos do eixo y definido pelo usuário.
plt.yticks(fontsize=10)  #  Tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  #  Habilita o tickmark do eixo direito.

#  Gera a legenda sem borda, define localização e o seu tamanho.
plt.legend(frameon =False, loc='upper right', fontsize=10)

#  Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex03.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)