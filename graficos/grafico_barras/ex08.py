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

x = np.arange(len(x2))  # 215 valores.

y = df['PREC']

fig, ax = plt.subplots(figsize=(6,3))  # Largura e altura da figura.

ax.bar(x, y, 0.75, color="blue", alpha=0.5)

# Título da figura.
plt.title('Precipitação mensal - 2003 a 2020', fontsize=8)

#  Formatação do eixo x.
plt.xlim(-1, 216, 1)  # Define o mínimo e o máximo valor do eixo x.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
# Rótulos do eixo x, tamanho da fonte e orientação.
plt.xticks(np.arange(0,len(x)-1,12), x1, fontsize=8)

#  Formatação do eixo y.
plt.ylabel('Precipitação (mm/mês)', fontsize=8)
plt.ylim(0, 500)
plt.yticks(np.arange(0, 505, step=50), fontsize=8)
plt.tick_params(axis='y', right=True)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex08.jpg', transparent=True, dpi=300, bbox_inches='tight', 
            pad_inches=0)  