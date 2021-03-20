import numpy as np
import matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12,6))

x = np.linspace(0, 5, 10)

# Espessura da linha.
ax.plot(x, x+1, color="black", linewidth=0.25)
ax.plot(x, x+2, color="black", linewidth=0.50)
ax.plot(x, x+3, color="black", linewidth=0.75)
ax.plot(x, x+4, color="black", linewidth=1.00)
ax.plot(x, x+5, color="black", linewidth=2.00)
ax.plot(x, x+6, color="black", linewidth=3.00)
ax.plot(x, x+7, color="black", linewidth=4.00)

# Adiciona texto para a espessura da linha.
ax.text(-0.19, 0.8, '0.25', fontsize=9, rotation=3)
ax.text(-0.19, 1.8, '0.50', fontsize=9, rotation=3)
ax.text(-0.19, 2.8, '0.75', fontsize=9, rotation=3)
ax.text(-0.19, 3.8, '1.00', fontsize=9, rotation=3)
ax.text(-0.19, 4.8, '2.00', fontsize=9, rotation=3)
ax.text(-0.19, 5.8, '3.00', fontsize=9, rotation=3)
ax.text(-0.19, 6.8, '4.00', fontsize=9, rotation=3)
ax.text(-0.19, 8, 'Espessura\nda\nlinha', fontsize=9,  rotation=3)

# Marcadores.
ax.plot(x, x+12, color="black", lw=1, ls='', marker='o', markersize=2)
ax.plot(x, x+13, color="black", lw=1, ls='', marker='o', markersize=3)
ax.plot(x, x+14, color="black", lw=1, ls='', marker='o', markersize=4)
ax.plot(x, x+15, color="black", lw=1, ls='', marker='o', markersize=5)
ax.plot(x, x+16, color="black", lw=1, ls='', marker='o', markersize=6)
ax.plot(x, x+17, color="black", lw=1, ls='', marker='o', markersize=7)
ax.plot(x, x+18, color="black", lw=1, ls='', marker='o', markersize=8)
ax.plot(x, x+19, color="black", lw=1, ls='', marker='o', markersize=9)
ax.plot(x, x+20, color="black", lw=1, ls='', marker='o', markersize=10)

# Adiciona texto para os marcadores.
ax.text(-0.15, 11.8,  '2', fontsize=9,  rotation=0)
ax.text(-0.15, 12.8, '3', fontsize=9,  rotation=0)
ax.text(-0.15, 13.8, '4', fontsize=9,  rotation=0)
ax.text(-0.15, 14.8, '5', fontsize=9,  rotation=0)
ax.text(-0.15, 15.8, '6', fontsize=9,  rotation=0)
ax.text(-0.15, 16.8, '7', fontsize=9,  rotation=0)
ax.text(-0.15, 17.8, '8', fontsize=9,  rotation=0)
ax.text(-0.15, 18.8, '9', fontsize=9,  rotation=0)
ax.text(-0.15, 19.8, '10', fontsize=9, rotation=0)
ax.text(-0.17, 21  , 'Tamanho\ndo\nmarcador', fontsize=9,  rotation=0)

# Desabilita os 4 eixos do gráfico.
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)
ax.tick_params(axis='x', which='both', top=False, bottom=False, labelbottom=False)

plt.savefig('ex05.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)