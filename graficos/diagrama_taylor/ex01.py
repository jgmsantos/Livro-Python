import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
import skill_metrics as sm
import pandas as pd

# Leitura do arquivo no formato ".csv".
data = pd.read_csv('../../dados/texto/cmip5/cmip5.csv',
                 sep=',', 
                 names=['OBS', 'M1', 'M2', 'M3', 'M4', 
                        'M5', 'M6', 'M7', 'M8', 'M9', 
                        'M10'])

# Define propriedades da figura.
rcParams["figure.figsize"] = [8.0, 6.4]
rcParams["lines.linewidth"] = 1  # Largura das linhas.
rcParams.update({"font.size": 12})  # Tamanho da fonte do eixo.

# Para editar o Diagrama de Taylor.
# /home/guilherme/miniconda3/envs/inpe/lib/python3.9/site-packages/skill_metrics/plot_taylor_axes.py

# Fecha qualquer ambiente gráfico para evitar erros na geração do diagrama.
plt.close("all")

obs_key = "OBS"  # Dado observado.

# Função para filtar apenas os modelos.
taylor_stats = [
    sm.taylor_statistics(data[obs_key], data[column])
    for column in data.columns
    if column != obs_key
]

# Função que calcula as métricas.
def make_arrange(taylor_stats, key):
    data = []
    data.append(taylor_stats[0][key][0])
    for stats in taylor_stats:
        data.append(stats[key][1])
    return np.array(data)

# Armazena os resultados em arranjos de sdev (desvio padrão), 
# crmsd (erro quadrático médio) e ccoef (correlação).
sdev = make_arrange(taylor_stats, 'sdev')
crmsd = make_arrange(taylor_stats, 'crmsd')
ccoef = make_arrange(taylor_stats, 'ccoef')

# print(sm.taylor_diagram())  # Descomentar para mais opções de formatação.

# Rótulos do gráfico.
label1 = ["OBS", "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10"]

# Rótulos que vão aparecer na legenda.
label2 = [
    "M1: ACCESS1-0",
    "M2: BCC-CSM1.1",
    "M3: BESM",
    "M4: CANESM",
    "M5: CCSM4",
    "M6: CNRM-CM5",
    "M7: CSIRO-MK3-6-0",
    "M8: FGOALS-G2",
    "M9: GFDL-CM3",
    "M10: GFDL-ESM2G",
]

# Intervalos de correlação que vão aparecer no gráfico.
intervalsCOR = np.concatenate((np.arange(0, 1.0, 0.2), [0.9, 0.95, 0.99, 1]))

# Plot do gráfico e sua formatação.
sm.taylor_diagram(
    sdev,
    crmsd,
    ccoef,
    styleOBS="-",
    colOBS="black",
    markerobs="o",
    titleOBS="Observação",
    markerLabel=label1,
    markerSize=9,
    markerColor="red",
    axismax=100.0,
    titleRMS="off",
    showlabelsRMS="off",
    tickRMS=[0.0],
    colSTD="black",
    styleSTD=":",
    widthSTD=1.0,
    tickSTD=np.arange(0, 125, 25),
    colCOR="blue",
    styleCOR="--",
    widthCOR=1.0,
    tickCOR=intervalsCOR,
)

# Título principal da figura, posição e tamanho da fonte.
plt.suptitle("Precipitação no bioma Amazônia", y=0.98, fontsize=13)

# Título do eixo x e tamanho da fonte.
plt.xlabel("GPCP", fontsize=10)
plt.xticks(fontsize=10)  #  Tamanha fonte dos rótulos do eixo x.

# Título do eixo y e tamanho da fonte.
plt.ylabel("Desvio padrão", fontsize=10)
plt.yticks(fontsize=10)  #  Tamanha fonte dos rótulos do eixo y.

# Posição x e y onde começa a inserir o nome dos modelos.
x = 110
y = 70

# Insere o nome dos modelos no gráfico como legenda.
for nome_modelo in label2:
    plt.text(x, y, nome_modelo, fontsize=9)
    y = y - 5

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig("ex01.jpg", transparent=True, dpi=300, bbox_inches="tight", 
            pad_inches=0)