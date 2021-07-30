import matplotlib.pyplot as plt
import pandas as pd

# Abertura do arquivo.
df = pd.read_csv('../../dados/texto/classificacao_vento.txt', 
                 sep= '\t', 
                 names=['Tipo', 'Frequencia'])

categoria = df['Tipo']
frequencia = df['Frequencia']

# Destaca (valor 0.1) o maior valor da série que é o terceiro 
# valor do arquivo classificacao_vento.txt.
explode = (0, 0, 0.1)

fig, ax = plt.subplots()

# Gera o plot.
# frequencia = frequência, a função calcula a porcentagem, 
# explode = destaca a maior fatia da pizza, labels = rórulos 
# que vão aparecer na pizza, autopct = formatação do número.
ax.pie(frequencia, 
       explode=explode, 
       labels=categoria, 
       autopct='%1.0f%%', 
       startangle=90, 
       colors=['cornflowerblue', 'palegreen', 'salmon'])
ax.axis('equal')

# Formatação do título da figura. y = distância do título para o 
# gráfico, fontsize = tamanho da fonte.
plt.title("Categorias de velocidade do vento", y=1.05, fontsize=12)

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex01.jpg', transparent=True, dpi=300, bbox_inches='tight', 
            pad_inches=0)