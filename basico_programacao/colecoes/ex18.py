import pandas as pd

direcao = pd.DataFrame(['N', 'ENE', 'ENE', 'E', 'E', 'E', 'E', 'ENE', 'ENE'])
#                        0     1      2     3    4    5    6     7      8  <= Posições.

# Verifica as linhas que são duplicadas por meio do seu índice.
direcao_duplicada = direcao.duplicated()

# Remove as linhas duplicadas.
duplicada = direcao.drop_duplicates()

#print(direcao_duplicada)

print(duplicada)