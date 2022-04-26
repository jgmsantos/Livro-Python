import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xarray as xr


# Função que insere uma linha horizontal em posições
# específicas do eixo y.
def insere_linha(estilo_linnha, posicao_y, espessura_linha, cor_linha):
    plt.axhline(
        linestyle=estilo_linnha, y=posicao_y, linewidth=espessura_linha, color=cor_linha
    )


# Função que insere os rótulos em posições específicas
# do eixo y. Complemento da função acima.
def insere_categoria(x, y, rotulo, tamanho_fonte):
    plt.text(x, y, rotulo, fontsize=tamanho_fonte)


# posição no eixo y para inserir as linhas horizontais
# de cada categoria do SPI.
lista_posicoes_y = [2, 1.5, 1, 0, -1, -1.5, -2]

# As categorias de SPI.
lista_categorias = [
    "Extremamente Úmido",
    "Muito Úmido",
    "Moderadamente Úmido",
    "Próximo do normal",
    "Extremamente seco",
    "Severamente seco",
    "Moderadamente seco",
    "Próximo do normal",
]

maximo_valor_y = 3.0  # Máximo valor do eixo y.
minimo_valor_y = -2.5  # Mínimo valor do eixo y.

# Onde inserir as categorias no eixo y.
lista_posicoes_categorias = [2.05, 1.55, 1.05, 0.80, -2.18, -1.68, -1.18, -0.92]

# Período de interesse.
data_inicial = "2019-01"
data_final = "2020-09"

# Cria a lista de meses para ser utilizado no gráfico.
x = [
    i.strftime("%Y%m")
    for i in pd.date_range(start=data_inicial, end=data_final, freq="MS")
]

largura_barra = 0.75

# Abertura do arquivo.
ds = xr.open_dataset("../../dados/netcdf/spi.nc", decode_times=False)

# Cria a unidade de tempo do arquivo por causa do "decode_times=False".
units, reference_date = ds.time.attrs["units"].split("since")
ds["time"] = pd.date_range(start=reference_date, periods=ds.sizes["time"], freq="MS")

# Seleciona o período de interesse, isto é, jan/2019 a dez/2020.
meses = ds.sel(time=slice(data_inicial, data_final))

# Seleciona o SPI de interesse:
# Formato: spi(time, spi, lat, lon) = (492, 6, 1, 1)
# Valor  => spi = 1, 3, 6, 12, 24, 36 meses
# Índice => spi = 0, 1, 2,  3,  4,  5
y1 = ds.sel(time=slice(data_inicial, data_final), lat=0, lon=0, lev=1)
y2 = y1["spi"]

# Separa os valores mínimos e máximos.
acima_limiar = np.maximum(y2 - 0, 0)
abaixo_limiar = np.minimum(y2, 0)

fig, ax = plt.subplots(figsize=(6, 3))  # Largura e altura da figura.

# Gera o plot com base nos limiares e separa o que
# é positivo (negativo) com vermelho (azul).
ax.bar(x, abaixo_limiar, 0.75, color="r", alpha=0.5)
ax.bar(x, acima_limiar, 0.75, color="b", bottom=abaixo_limiar, alpha=0.5)

# Função que insere as linhas horizontais em posições
# específicas do eixo y.
# Estilo da linha, posição y, posição x e cor.
[insere_linha("--", y, 0.5, "black") for y in lista_posicoes_y]

# Função que insere os rótulos das categorias do SPI
# em posições específicas do eixo y.
[
    insere_categoria(-0.3, y, rotulos, 8)
    for y, rotulos in zip(lista_posicoes_categorias, lista_categorias)
]

# Título da figura.
plt.title("SPI no bioma Pantanal", fontsize=8)

#  Formatação do eixo x.
plt.xlim(-0.5, len(x) - 0.5)  # Define o mínimo e o máximo valor do eixo x.
# Rótulos do eixo x, tamanho e orientação.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

#  Formatação do eixo y:
plt.ylabel("SPI (Adimensional)", fontsize=8)
plt.ylim(minimo_valor_y, maximo_valor_y - 0.5)
# Define o mínimo e máximo valor do eixo y e o tamanho dos seus rótulos.
plt.yticks(np.arange(minimo_valor_y, maximo_valor_y, step=0.5), fontsize=8)
plt.tick_params(axis="y", right=True)  # Habilita o tickmark do eixo direito.

plt.xticks(np.arange(0, len(x)), x, fontsize=8)

#  Formatação do eixo y.
plt.ylabel("SPI (Adimensional)", fontsize=8)
# Define o mínimo e máximo valor do eixo y.
plt.ylim(minimo_valor_y, maximo_valor_y - 0.5)
# Define o mínimo e máximo valor do eixo y e o tamanho dos seus rótulos.
plt.yticks(np.arange(minimo_valor_y, maximo_valor_y, step=0.5), fontsize=8)
# Habilita o tickmark do eixo direito.
plt.tick_params(axis="y", right=True)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig("ex06.jpg", transparent=True, dpi=300, bbox_inches="tight", pad_inches=0)
