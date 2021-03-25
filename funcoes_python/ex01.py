import numpy as np
import math

# Gera 11 elementos a cada com intervalo de 0.5.
x = np.linspace(0, 5, 11)
print(x)  # [0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5 5. ]

# Gera 5 elementos a cada com intervalo de 2.5.
x = np.linspace(0, 10, 5)
print(x)  # [ 0.   2.5  5.   7.5 10. ]

# Gera números aleatórios.
x = np.random.random(5)
print(x)  # [0.14640476 0.81601629 0.85883815 0.78358921 0.99644288]

# Exibe o tipo de dado utilizado.
x = [1, 2., 3, 4]
print(type(x))  # int64

# Gera uma lista com valores entre 0 e 19. O valor 20 não é gerado.
x = np.arange(20) 
print(x)  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

# Gera valores de 0 a 100 com passo 10. O valor 100 não é gerado.
x = np.arange(0,100,10)
print(x)  # [ 0 10 20 30 40 50 60 70 80 90]

# Gera uma lista com valores entre 1 e 12. O valor 13 não é gerado.
x = np.arange(1,13)
print(x)  # [ 1  2  3  4  5  6  7  8  9 10 11 12]

# Ordena o arranjo de forma crescente.
x = [10, 4, 50, 1, 15]
x.sort()
print(x)  # [1, 4, 10, 15, 50]

# Ordena o arranjo de forma decrescente.
x = [10, 4, 50, 1, 15]
x.sort(reverse=True)
print(x)  # [1, 4, 10, 15, 50]

# Exibe o tipo do dado.
x = np.array([-10, 10, 20, 30])
print(x.dtype)  # int64

# Arredondamento para o inteiro mais próximo (math.ceil).


print(math.ceil(1.1))   # 2
print(math.ceil(5.3))   # 6
print(math.ceil(-5.6))  # -5 
print(math.ceil(22.4))  # 23
print(math.ceil(10.0))  # 10

# Arredondamento para o menor inteiro mais próximo (math.floor).
print(math.floor(1.1))   # 1
print(math.floor(5.3))   # 5
print(math.floor(-5.6))  # -6 
print(math.floor(22.4))  # 22
print(math.floor(10.0))  # 10

# Retorna o número de elementos.
x = [1, 2, 3, 4, 5]  
print(len(x))  # 5

x = [[1, 2, 3, 4, 5],[6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
print(len(x))  # 3

# Média dos valores.
x = [1, 2, 3, 4, 5]
y = np.mean(x)
print(y)  # 3.0

# Desvio padrão dos valores.
x = [[1, 2, 3, 4, 5]]
y = np.std(x)
print(y)  # 1.4142135623730951

# String maiúscula.
x = 'egUa, mAno!'
x = x.upper()
print(x)

# String minúscula.
x = x.lower()
print(x)

# String com a primeira letra em maiúscula.
x = 'egUa, mAno!'
x = x.title()  # Egua, Mano!
print(x)

# Divide a string.
x = x.split()
print(x)

# Interagindo com o sistema.
# Link: https://docs.python.org/3/library/os.html

import os

# Visualizar os métodos do os.
print(dir(os))

# Retornar o caminho do diretório corrente.
x = os.getcwd()
print(x)

## Revome um diretório 
#os.rmdir('nome_diretorio')
#
## Criar um diretório.
#os.mkdir('nome_diretorio')

# Listar o conteúdo do diretório corrente.
x = os.listdir()
print(x)

# Remover arquivo.
os.remove('x.txt')

# Renomear arquivo.
os.rename('oldfile','newfile')