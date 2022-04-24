import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Warning
from yellowbrick.regressor import ResidualsPlot


# Abertura do arquivo.
ds = pd.read_csv(
    "../../../dados/texto/variaveis_meteorologicas.txt",
    sep="\t",
    names=["DATA", "UR", "TEMP", "PREC", "VELVENTO", "DIRVENTO"],
)

# Importação das variáveis de interesse.
x = ds["PREC"]  # Variável independente.
y = ds["UR"]  # Variável dependente.

x = np.array(x)  # Converte para array.

# Cálculo da correlação.
r = np.corrcoef(x, y)  # r = 0.4755698
r = r[0][1]  # O resultado é uma matriz.

x = x.reshape(-1, 1)  # Converte de 1D para 2D.

plt.figure(figsize=(8, 4))  # Largura e altura da figura.

# Criação do modelo de regressão.
modelo = LinearRegression()
modelo.fit(x, y)

# Imprime a previsão de Umidade Relativa caso a precipitação
# seja de 300 mm/mês. É um exemplo.
print("++++++++++++++++++++++++++++++++++++++++")
print("Previsão de UR quando PREC = 300 mm/mês:", modelo.predict([[300]]))
print("++++++++++++++++++++++++++++++++++++++++")

# Equação de Regressão: y = a*x + b.
a = modelo.coef_  # Coeficiente angular (a).
b = modelo.intercept_  # Onde intercepta no eixo y (b).

# Primeiro plot.
# Visualiza o dado e a reta de regressão.
plt.scatter(x, y, color="blue", marker="o", label="Dado original")  # Dado.
plt.plot(
    x, modelo.predict(x), color="red", label=f"y={a[0]:.3f}x+{b:.3f} | R={r:.2f}"
)  # Reta de regressão.
plt.legend()  # Mostra a legenda.
# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig("ex01a.jpg", transparent=True, dpi=300, bbox_inches="tight", pad_inches=0)

plt.clf()  # Limpa o ambiente gráfico para plotar o segundo gráfico.

# Segundo plot.
# Visualiza os residuais e o histograma.
visualizador = ResidualsPlot(modelo)
visualizador.fit(x, y)
# visualizador.poof()  # Descomentar para a ver a figura.
# Salva a figura no formato ".jpg".
plt.savefig("ex01b.jpg", transparent=True, dpi=300, bbox_inches="tight", pad_inches=0)
