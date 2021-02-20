import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('../../../dados/texto/umidade_relativa_temperatura.txt', sep= '\t', names=['Data', 'Umidade Relativa', 'Temperatura'])

x = df['Umidade Relativa']  # Importa os valores de umidade relativa.

# Valores do histograma.
valores_histograma = np.histogram(x, bins=10)
print(valores_histograma)

fig, ax = plt.subplots(figsize=(6,3))  # Largua e altura da figura.

ax.hist(x, bins=10, histtype='bar', color='wheat', alpha=0.75, rwidth=0.8) 

# Título principal da figura.
plt.title('Histograma de Umidade Relativa', fontsize=10)

# Formatação do eixo x.
plt.xlabel('Classes', fontsize=8)  # Título do eixo x e o seu tamanho.
plt.xticks(fontsize=8)  # Tamanho dos rótulos do eixo x.
plt.xlim(0, 100)  # Define o mínimo e o máximo valor do eixo x.
ax.set_xticks(ticks=range(0, 105, 10))  # Rótulos do eixo y definido pelo usuário.

# Formatação do eixo y.
plt.ylabel('Frequência', fontsize=10)  # Título do eixo y e o seu tamanho.
ax.set_ylim(0, 35)  # Mínimo e máximo valor do eixo y.
ax.set_yticks(ticks=range(0, 40, 5))  # Rótulos do eixo y definido pelo usuário.
plt.yticks(fontsize=8)  # Tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex01.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)