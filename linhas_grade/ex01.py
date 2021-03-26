import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../dados/texto/precipitacao.txt', sep= '\t', 
                  names=['Mês', 'Climatologia', '2019', '2020'])

x = df['Mês']
y = df['Climatologia']

plt.plot(x, y) 

# Visualiza as grades horizontal e vertical.
# alpha = transparência das linhas, lw = espessura das linhas e 
# color = cor das linhas.
# Opções: which='major' ou 'minor', axis='x' ou 'y' ou 'both'.
plt.grid(alpha=0.5, ls='--', lw=1, color='gray')

plt.tick_params(axis='y', right=True)

plt.savefig('ex01.jpg', transparent=True, dpi=300, 
             bbox_inches='tight', pad_inches=0)