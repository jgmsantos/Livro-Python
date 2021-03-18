import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Função que adiciona o label nas barras e a unidade.
def define_label (ax, rects, values):
    for rect, value in zip(rects, values):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height, f'{value}', ha='center', va='bottom', fontsize=8)

# Abertura do arquivo vento_direcao_velocidade_porcentagem.txt com o separador TAB. Adiciona também o título de cada coluna.
# A primeira coluna é o mês, a segunda, a climatologia, a terceria, o ano de 2019 e a quarta, o ano de 2020.
df = pd.read_csv('../../dados/texto/vento_direcao_velocidade_porcentagem.txt', sep= '\t', names=['Direção', 'dirPorcentagem', 'velPorcentagem'])

x = df['Direção']  # Importa a Direção no formato string.
y = df['velPorcentagem']  # Importa a coluna com os valores percentuais.

r1 = np.arange(16)  # [0, 1, 2, ..., 15]. Vetor com os índices do eixo x.
x1 = [y - 0.13 for y in r1]
x2 = [y + 0.13 for y in r1]

fig, ax = plt.subplots(figsize=(7, 4))  # Largura e altura da figura.

# Gera o plot.
plt.bar(x, y, color='bisque', width=0.6, alpha=0.90) 

# Chama a função para adicionar os valores em cada uma das barras.
define_label(ax, ax.containers[0].patches, y)

# Título principal da figura.
plt.title('Categorias de Velocidade do Vento - Julho a Outubro de 2020', fontsize=8)

# Formatação do eixo x.
plt.xlabel('Direção', fontsize=8)  # Título do eixo x e o seu tamanho.
plt.xticks(fontsize=8)  # Tamanho dos rótulos do eixo x.
# Rótulos do eixo y definido pelo usuário.
ax.set_xticks(ticks=['N', 'NNE', 'NE', 'ENE', 'E', 'SE', 'ESE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'])  

#  Formatação do eixo y.
plt.ylabel('Velocidade do vento (m/s)', fontsize=8)  #  Título do eixo y e o seu tamanho.
plt.yticks(fontsize=8)  #  Tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  #  Habilita o tickmark do eixo direito.
ax.set_ylim(0, 4)  #  Mínimo e máximo valor do eixo y.

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex09.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)