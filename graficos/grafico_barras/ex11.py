import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Abertura do arquivo utilizando o separador espaço e adicionando título como primeira linha.
df = pd.read_csv('../../dados/texto/variaveis_meteorologicas.txt', sep= '\t', names=['Data','UR', 'TEMP', 'PREC', 'VEL_VENTO', 'DIR_VENTO'])

x = np.arange(123)  # Desde 01/07/2020 31/10/2020 = 123 dias.
dias = ['01/07/2020', '15/07/2020', '01/08/2020', '15/08/2020', '01/09/2020', '15/09/2020', '01/10/2020', '15/10/2020', '31/10/2020']

y = df['PREC']

# Gera o plot com base nos limiares e separa o que é positivo (negativo) com vermelho (azul).
fig, ax = plt.subplots(figsize=(6,3))  # Largua e altura da figura.

ax.bar(x, y, 0.75, color="blue", alpha=0.5)

# Título da figura.
plt.title('Precipitação: Serra do Cipó', fontsize=10)

#  Formatação do eixo y.
plt.ylabel('Precipitação (mm/dia)', fontsize=10)  # Tamanho do título do eixo y.
plt.ylim(0, 30)  # Define o mínimo e máximo valor do eixo y.
plt.yticks(np.arange(0, 35, step=5), fontsize=7)  # Define o mínimo e máximo valor do eixo y, tamanho dos seus rótulos.
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

#  Formatação do eixo x.
plt.xlim(-1, 124, 1)  # Define o mínimo e o máximo valor do eixo x.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
plt.xticks([0, 14, 31, 45, 62, 76, 92, 106, 122], dias, fontsize=7)  # Rótulos do eixo x, tamanho e orientação.

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex11.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)