import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('../../dados/texto/pr.GPCP.txt', sep='\t', names=['Ano', 'Mês', 'Prec'])

Mes = ['Janeiro','Feveiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

dados = df.pivot(index='Mês', columns='Ano', values='Prec')

#fig, ax = plt.subplots()

f, (ax, cbar_ax) = plt.subplots(2, gridspec_kw={"height_ratios": (.9, .05), "hspace": .3}, figsize=(8,5))

# Plot da figura.
ax = sns.heatmap(dados, ax=ax, annot=True, fmt="d", square=True, annot_kws={"size": 5},  yticklabels=Mes, cbar_ax=cbar_ax, cbar_kws={"orientation": "horizontal"}, cmap='magma', vmin=0, vmax=300, linewidths=0.5)

# Título da figura.
ax.set_title("Heatmap de precipitação (mm/mês) na Amazônia", fontsize = 8)

# Tamanho dos rótulos dos eixos x e y.
ax.tick_params(labelsize=8)  

# Tamanho da fonte da barra de cores.
cbar_ax.tick_params(labelsize=8) 

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex01.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)