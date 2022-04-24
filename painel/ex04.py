import matplotlib.pyplot as plt
import pandas as pd

# Leitura do arquivo.
df = pd.read_csv(
    "../dados/texto/ERA5.Climatologia.txt",
    sep="\t",
    names=["Mês", "Umidade Relativa", "Temperatura", "VelVento", "DirVento"],
)

mes = df["Mês"]
ur = df["Umidade Relativa"]
temp = df["Temperatura"]
vel = df["VelVento"]
dir = df["DirVento"]

nlin = 2  # 2 linhas.
ncol = 2  # 2 coluna.

# O figsize define o tamanho e a largura da figura.
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nlin, ncol, figsize=(12, 9))

# Plot de cada série de dados.
ax1.bar(mes, ur, color="green", alpha=0.5, width=0.6)
ax2.bar(mes, temp, color="red", alpha=0.5, width=0.6)
ax3.bar(mes, vel, color="orange", alpha=0.5, width=0.6)
ax4.bar(mes, dir, color="blue", alpha=0.5, width=0.6)

# Título principal da figura.
fig.suptitle("Variáveis meteorológicas", fontsize=14)

# Título de cada figura e o seu tamanho.
ax1.set_title("Climatologia de Umidade Relativa", fontsize=14)
ax2.set_title("Climatologia de Temperatura", fontsize=14)
ax3.set_title("Climatologia de Velocidade do vento", fontsize=14)
ax4.set_title("Climatologia de Direção do vento", fontsize=14)

# Formatação do eixo x.
ax1.set_xlabel("Mês", fontsize=14)
ax2.set_xlabel("Mês", fontsize=14)
ax3.set_xlabel("Mês", fontsize=14)
ax4.set_xlabel("Mês", fontsize=14)

# Habilita o tickmark do eixo inferior e define o
# tamanho dos rótulos do eixo x inferior.
ax1.tick_params(axis="x", top=True, labelsize=14)
ax2.tick_params(axis="x", top=True, labelsize=14)
ax3.tick_params(axis="x", top=True, labelsize=14)
ax4.tick_params(axis="x", top=True, labelsize=14)

# Formatação do eixo y.
ax1.set_ylabel("Umidade Relativa (%)", fontsize=14)
ax2.set_ylabel("Temperatura (ºC)", fontsize=14)
ax3.set_ylabel("Velocidade do vento (m/s)", fontsize=14)
ax4.set_ylabel("Direção do vento (graus)", fontsize=14)

# Habilita o tickmark do eixo direito e define o tamanho dos
# rótulos do eixo y esquerdo.
ax1.tick_params(axis="y", right=True, labelsize=14)
ax2.tick_params(axis="y", right=True, labelsize=14)
ax3.tick_params(axis="y", right=True, labelsize=14)
ax4.tick_params(axis="y", right=True, labelsize=14)

# Define os valores mínimo e máximo do eixo y de cada ax.
ax1.set_ylim(0, 100)
ax2.set_ylim(16, 24)
ax3.set_ylim(0, 2)
ax4.set_ylim(0, 100)

# Define os rótulos que vão aparecer no eixo y.
ax1.set_yticks(ticks=[0, 20, 40, 60, 80, 100])
ax2.set_yticks(ticks=[16, 18, 20, 22, 24])
ax3.set_yticks(ticks=[0, 0.5, 1.0, 1.5, 2.0, 2.5])
ax4.set_yticks(ticks=[0, 25, 50, 75, 100])

fig.tight_layout()  # Ajusta automaticamente os espaços entre as figuras.

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig("ex04.jpg", transparent=True, dpi=300, bbox_inches="tight", pad_inches=0)
