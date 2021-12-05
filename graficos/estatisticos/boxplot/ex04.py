import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('../../../dados/texto/cmip5/cmip5.csv', 
                 sep=',', 
                 names=['OBS', 'M1', 'M2', 'M3', 'M4', 
                        'M5', 'M6', 'M7', 'M8', 'M9', 
                        'M10'])

obs = df['OBS']
m1 = df['M1']
m2 = df['M2']
m3 = df['M3']
m4 = df['M4']
m5 = df['M5']
m6 = df['M6']
m7 = df['M7']
m8 = df['M8']
m9 = df['M9']
m10 = df['M10']

fig, ax = plt.subplots(figsize=(6,3))  # Largua e altura da figura.

# Gera o plot.
plt.boxplot([obs, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10], 
             showfliers=True, 
             notch= False, 
             patch_artist=True, 
             showmeans=True, 
             meanline=True)

box = plt.boxplot([obs, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10], 
                  patch_artist=True)

colors = ['silver', 'tan', 'powderblue', 'pink', 'moccasin', 
          'lightgreen', 'deepskyblue', 'slateblue', 'violet', 'tomato', 
          'peru']
 
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Título principal da figura.
plt.title('Boxplot de Precipitação - 1979 a 2005', fontsize=8)

# Formatação do eixo x.
plt.xlim(0, 12)
plt.ylabel('Precipitação (mm/mês)', fontsize=8)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
plt.xticks(ticks=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 
           labels=['OBSERVADO', 'ACCESS1-0', 'BCC-CSM1.1', 'BESM', 'CANESM', 
                   'CCSM4', 'CNRM-CM5', 'CSIRO-MK3-6-0', 'FGOALS-G2', 'GFDL-CM3', 
                   'GFDL-ESM2G'], fontsize=8)  # Rótulos do eixo x definido 
                                               # pelo usuário.

# Formatação do eixo y.
plt.ylim(0, 400)
plt.yticks(ticks=range(0, 410, 50), fontsize=8)
plt.tick_params(axis='y', right=True)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex04.jpg', transparent=True, dpi=300, bbox_inches='tight', 
            pad_inches=0)