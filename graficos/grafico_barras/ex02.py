import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Abertura do arquivo temperatura.txt com o separador TAB. Adiciona 
# também o título de cada coluna. A primeira coluna é o mês, a segunda, 
# a climatologia, a terceria, o ano de 2019 e a quarta, o ano de 2020.
df = pd.read_csv('../../dados/texto/precipitacao.txt', 
                 sep= '\t', 
                 names=['Mês', 'Climatologia', '2019', '2020'])

x = df['Mês']  # Importa os valores da coluna Mês.
y1 = df['Climatologia']  # Importa os valores da coluna Climatologia.
y2 = df['2019']  # Importa os valores da coluna 2019.
y3 = df['2020']  # Importa os valores da coluna 2020.

plt.figure(figsize=(8, 4))  # Largura e altura da figura.

# Posição onde serão geradas as barras.
x1 = np.arange(len(y1))  # Valores do eixo x para desenhar a primeira barra.
x2 = [y + 0.25 for y in x1]  # Valores do eixo x para desenhar a segunda barra.
x3 = [y + 0.25 for y in x2]  # Valores do eixo x para desenhar a terceira barra.

# Plot da figura. color = cor da barra, width = largura da barra, 
# label = nome que vai aparecer na legenda e alpha = aplica efeito 
# de transparência na barra.
plt.bar(x1, y1, color='green', width=0.25, label='Climatologia', alpha=0.30)
plt.bar(x2, y2, color='red', width=0.25, label='2019', alpha=0.30)
plt.bar(x3, y3, color='blue', width=0.25, label='2020', alpha=0.30)

# Título principal da figura.
plt.title('Precipitação no bioma Amazônia')

# Formatação do eixo x.
plt.xlabel('Mês', fontsize=8)  # Título do eixo x e o tamanho da fonte.
# Adiciona os rótulos e define o tamanho deles.
plt.xticks([r + 0.25 for r in range(len(y1))], x, fontsize=8)
plt.xlim(-0.5, 12)  # Mínimo e máximo valor do eixo x.

# Formatação do eixo y.
plt.ylabel('Precipitação (mm/mês)', fontsize=8)
plt.ylim(0, 300)  # Mínimo e máximo valor do eixo y.
# Rótulos do eixo y definido pelo usuário.
plt.yticks(ticks=[0, 50, 100, 150, 200, 250, 300])  
plt.yticks(fontsize=8)  # Tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

# Gera a legenda sem borda, define localização e o tamanho da fonte.
plt.legend(frameon=False, loc='upper right', fontsize=8)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex02.jpg', transparent=True, dpi=300, bbox_inches='tight', 
            pad_inches=0)