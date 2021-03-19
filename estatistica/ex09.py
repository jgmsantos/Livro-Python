import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Abertura do arquivo utilizando o separador TAB e adiciona o título como primeira linha.
df = pd.read_csv('../dados/texto/variaveis_meteorologicas.txt', sep= '\t', 
                  names=['Data','UR','Temp','PREC','VelVento','DirVento'])

x = df['UR']
y = df['Temp']

res = stats.linregress(x, y)  # Calcula a regressão.

print(res)

# LinregressResult(slope=0.009648198915792867, intercept=19.804621140772895, 
# rvalue=0.036961733120948005, pvalue=0.5890198667365112, 
# stderr=0.017831594203681106, intercept_stderr=1.3324861298480515)

r2 = res.rvalue**2  # Calcula o R**2.

# Gera o gráfico.
plt.plot(x, y, 'o', label='Dado original')
plt.plot(x, res.intercept + res.slope*x, 'r', label=f'y={res.slope:.4f}x+{res.intercept:.3f}')
plt.legend()
# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex09.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)


