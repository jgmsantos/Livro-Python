import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Função que adiciona o label nas barras e a unidade de porcentagem (%).
def define_label (ax, rects, values):
    for rect, value in zip(rects, values):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height, f'{value}%', ha='center', va='bottom')

# Abertura do arquivo temperatura.txt com o separador TAB. Adiciona também o título de cada coluna.
# O arquivo tem formato de 12 linhas por 4 colunas. A primeira coluna é o mês, a segunda, a climatologia, 
# a terceria, o ano de 2019 e a quarta, o ano de 2020.
# Utiliza o separador '\t' que quer dizer TAB e cria o título para cada uma das colunas.
df = pd.read_csv('../../dados/texto/vento_direcao_velocidade_porcentagem.txt', sep= '\t', names=['Direção', 'dirPorcentagem', 'velPorcentagem'])

x = df['Direção']  # Importa a Direção no formato string.
y = df['dirPorcentagem']  # Importa a coluna com os valores percentuais.

r1 = np.arange(16)  # [0, 1, 2, ..., 15]. Vetor com os índices do eixo x.
x1 = [y - 0.13 for y in r1]
x2 = [y + 0.13 for y in r1]

# Comprimento e altura da figura.
fig, ax = plt.subplots(figsize=(7, 4))

# Gera o plot.
plt.bar(x, y, color='blue', label='Precipitação', width=0.6, alpha=0.30) 

# Chama a função para adicionar os valores em cada uma das barras.
define_label(ax, ax.containers[0].patches, y)

# Título principal da figura.
plt.title('Direção predominante do vento - Julho a Outubro/2020')

# Formatação do eixo x.
plt.xlabel('Direção', fontsize=10)  # Título do eixo x e o seu tamanho.
plt.xticks(fontsize=10)  # Tamanho dos rótulos do eixo x.
# Rótulos do eixo y definido pelo usuário.
ax.set_xticks(ticks=['N', 'NNE', 'NE', 'ENE', 'E', 'SE', 'ESE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'])  

#  Formatação do eixo y.
plt.ylabel('Frequência (%)', fontsize=10)  #  Título do eixo y e o seu tamanho.
plt.yticks(fontsize=10)  #  Tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  #  Habilita o tickmark do eixo direito.
ax.set_ylim(0, 45)  #  Mínimo e máximo valor do eixo y.

#   Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex08.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)