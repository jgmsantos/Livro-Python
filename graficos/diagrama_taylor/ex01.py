import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
import skill_metrics as sm
import pandas as pd

# Leitura do arquivo no formato ".csv".
data = pd.read_csv('../../dados/texto/cmip5/cmip5.csv')

# Define propriedades da figura.
rcParams["figure.figsize"] = [8.0, 6.4]
rcParams['lines.linewidth'] = 1  # Largura das linhas.
rcParams.update({'font.size': 12})  # Tamanho da fonte do eixo.

# Fecha qualquer ambiente gráfico para evitar erro na geração do diagrama.
plt.close('all')

# São geradas 3 informações:
# {'ccoef': array([1.        , 0.82997571]), 'crmsd': [0.0, 47.498368220553665], 'sdev': [54.80676311679932, 81.84068894654936]}
# 1) Correlação da série x com x e x com y.
# 2) RMSD da série x com x e x com y.
# 3) Desvio padrão da série x e y.
taylor_stats1  = sm.taylor_statistics(data['Obs'], data['M1'])
taylor_stats2  = sm.taylor_statistics(data['Obs'], data['M2'])
taylor_stats3  = sm.taylor_statistics(data['Obs'], data['M3'])
taylor_stats4  = sm.taylor_statistics(data['Obs'], data['M4'])
taylor_stats5  = sm.taylor_statistics(data['Obs'], data['M5'])
taylor_stats6  = sm.taylor_statistics(data['Obs'], data['M6'])
taylor_stats7  = sm.taylor_statistics(data['Obs'], data['M7'])
taylor_stats8  = sm.taylor_statistics(data['Obs'], data['M8'])
taylor_stats9  = sm.taylor_statistics(data['Obs'], data['M9'])
taylor_stats10 = sm.taylor_statistics(data['Obs'], data['M10'])

# Armazena os resultados em arranjos de sdev, crmsd e ccoef.
# Desvio padrão.
sdev = np.array([taylor_stats1['sdev'][0], taylor_stats1['sdev'][1], taylor_stats2['sdev'][1], taylor_stats3['sdev'][1], 
                 taylor_stats4['sdev'][1], taylor_stats5['sdev'][1], taylor_stats6['sdev'][1], taylor_stats7['sdev'][1], 
                 taylor_stats8['sdev'][1], taylor_stats9['sdev'][1], taylor_stats10['sdev'][1]])

# RMSD.
crmsd = np.array([taylor_stats1['crmsd'][0], taylor_stats1['crmsd'][1], taylor_stats2['crmsd'][1], taylor_stats3['crmsd'][1], 
                 taylor_stats4['crmsd'][1], taylor_stats5['crmsd'][1], taylor_stats6['crmsd'][1], taylor_stats7['crmsd'][1], 
                 taylor_stats8['crmsd'][1], taylor_stats9['crmsd'][1], taylor_stats10['crmsd'][1]])

# Correlação.
ccoef = np.array([taylor_stats1['ccoef'][0], taylor_stats1['ccoef'][1], taylor_stats2['ccoef'][1], taylor_stats3['ccoef'][1], 
                 taylor_stats4['ccoef'][1], taylor_stats5['ccoef'][1], taylor_stats6['ccoef'][1], taylor_stats7['ccoef'][1], 
                 taylor_stats8['ccoef'][1], taylor_stats9['ccoef'][1], taylor_stats10['ccoef'][1]])

# print(sm.taylor_diagram())  # Descomentar para mais opções de formatação.

# Rótulos que vão aparacer na legenda.
label = ['GPCP','ACCESS1-0','BCC-CSM1.1','BESM','CANESM',
         'CCSM4','CNRM-CM5','CSIRO-MK3-6-0','FGOALS-G2','GFDL-CM3',
         'GFDL-ESM2G']

# Intervalos de correlação que vão aparecer no gráfico.
intervalsCOR = np.concatenate((np.arange(0,1.0,0.2), [0.9, 0.95, 0.99, 1]))

# Plot do gráfico e sua formatação.
sm.taylor_diagram(sdev, crmsd, ccoef,
                  styleOBS='-', colOBS='red', markerobs='o', titleOBS='Observação', markerLabel=label, markerSize=5,
                  markerColor='y', markerLegend= 'on',
                  axismax=100.0,
                  titleRMS='off', showlabelsRMS='off', tickRMS=[0.0],
                  colSTD='black', styleSTD=':', widthSTD=1.0, tickSTD=np.arange(0, 125, 25), 
                  colCOR='blue', styleCOR='--', widthCOR=1.0, tickCOR=intervalsCOR)

# Título principal da figura.
plt.suptitle('Precipitação no bioma Amazônia', y=0.88, fontsize=13)

# Título do eixo x e o seu tamanho.
plt.xlabel('Observação', fontsize=10)
plt.xticks(fontsize=10)  #  Tamanho dos rótulos do eixo x.

# Título do eixo y e o seu tamanho.
plt.ylabel('Desvio padrão', fontsize=10)
plt.yticks(fontsize=10)  #  Tamanho dos rótulos do eixo y.

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex01.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)