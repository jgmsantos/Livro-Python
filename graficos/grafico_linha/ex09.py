import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leitura do arquivo no formato ".csv".
data = pd.read_csv('../../dados/texto/cmip5/cmip5.csv')

x = np.arange(0, 36, 1)  # Vetor com 36 posições (36 meses).

# Leitura do dado observado. Leitura apenas dos 36 primeiros tempos (36 meses).
obs = data['Obs'][0:36]
obs_std = np.std(obs)  # Cálculo do desvio padrão.

# Leitura dos dados dos modelos. Leitura apenas dos 36 primeiros tempos (36 meses).
m1 = data['M1'][0:36]
m2 = data['M2'][0:36]
m3 = data['M3'][0:36]
m4 = data['M4'][0:36]

# Largura e altura da figura.
fig, ax = plt.subplots(figsize=(8, 4))

## Gera o plot.
ax.plot(x, obs, marker='o', color='black', linestyle='solid', linewidth=3, label='Observado')
ax.plot(x, m1, color='red', linestyle='solid', linewidth=2, label='Modelo1')
ax.plot(x, m2, color='blue', linestyle='solid', linewidth=2, label='Modelo2')
ax.plot(x, m3, color='orange', linestyle='solid', linewidth=2, label='Modelo3')
ax.plot(x, m4, color='green', linestyle='solid', linewidth=2, label='Modelo4')

# Curva com o desvio padrão.
ax.fill_between(x, obs - obs_std, obs + obs_std, alpha=0.15, color='gray', label='Desvio Padrão')

# Gera a legenda sem borda, define localização e o tamanho da fonte.
plt.legend(frameon =False, loc='upper right', fontsize=6)

# Título principal da figura.
plt.title('Precipitação', fontsize=8)

# Formatação do eixo x.
plt.xlabel('Mês', fontsize=8)  # Título do eixo x e o tamanho da fonte.
plt.xticks(fontsize=8)  # Tamanho dos rótulos do eixo x.
ax.set_xlim(0, 35)  # Mínimo e máximo valor do eixo x.
plt.xticks([0, 6, 12, 18, 24, 30, 35], ['Jan1980', 'Jul1980', 'Jan1981', 'Jul1981', 'Jan1982', 'Jul1982', 'Dez1982'], fontsize=8)  

# Formatação do eixo y.
plt.ylabel('Precipitação (mm/mês)', fontsize=8)  # Título do eixo y e o tamanho da fonte.
ax.set_ylim(0, 400)  # Mínimo e máximo valor do eixo y.
ax.set_yticks(ticks=[0, 100, 200, 300, 400])  # Rótulos do eixo y definido pelo usuário.
plt.yticks(fontsize=8)  # Tamanho dos rótulos do eixo y.
plt.tick_params(axis='y', right=True)  # Habilita o tickmark do eixo direito.

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex09.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)
