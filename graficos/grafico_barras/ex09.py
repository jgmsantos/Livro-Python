import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Abertura do arquivo utilizando o separador TAB e adiciona o título 
# como primeira linha.
df = pd.read_csv('../../dados/texto/variaveis_meteorologicas.txt', 
                 sep= '\t', 
                 names=['Data','UR','Temp','PREC','VelVento','DirVento'])

# Período de interesse.
data_inicial = "2003-01"
data_final = "2020-12"

# Cria a lista de 12 meses para ser utilizado 
# no gráfico (200301, 200401, ..., 202001).
x1 = [i.strftime("%Y%m") for i in pd.date_range(start=data_inicial, 
     end=data_final, freq='12M')]

# Cria a lista com todos os meses desde 200301 a 202012.
x2 = [i.strftime("%Y%m") for i in pd.date_range(start=data_inicial, 
     end=data_final, freq='MS')]

x = np.arange(len(x2))  # 215.

ur = df['UR']
temp = df['Temp']

fig, ax = plt.subplots(figsize=(6,3))  # Largua e altura da figura.

# Plot do gráfico de barra.
ax.bar(x, ur, 0.75, color="green", alpha=0.5, label='Umidade Relativa')

ax2 = ax.twinx()

# Plot do gráfico de linha.
ax2.plot(x, temp, color="chocolate", alpha=0.8, label='Temperatura')

# Título da figura.
plt.title('Umidade Relativa e Temperatura - 2003 a 2020', fontsize=8)

#  Formatação do eixo x.
ax.set_xlim(-1, 216, 1)  # Define o mínimo e o máximo valor do eixo x.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
# Rótulos do eixo x, tamanho e orientação.
plt.xticks(np.arange(0,len(x)-1,12), x1, fontsize=8)

#  Formatação do eixo y esquerdo.
ax.set_ylabel('Umidade Relativa (%)', fontsize=8)
ax.set_ylim(0, 100)
ax.set_yticks(np.arange(0, 105, step=10))
ax.tick_params(labelsize=8)

#  Formatação do eixo y direito.
ax2.set_ylabel('Temperatura (ºC)', fontsize=8)
ax2.set_ylim(15, 25)
ax2.set_yticks(np.arange(15, 26, step=1))
ax2.tick_params(labelsize=8)

# Gera a legenda sem borda, define localização e o seu tamanho.
ax.legend(frameon =False, 
          loc='upper left', 
          fontsize=8, 
          bbox_to_anchor=(0.4, 0.96))
ax2.legend(frameon =False, 
           loc='upper left', 
           fontsize=8, 
           bbox_to_anchor=(0.4, 1.02))

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex09.jpg', transparent=True, dpi=300, bbox_inches='tight', 
            pad_inches=0)