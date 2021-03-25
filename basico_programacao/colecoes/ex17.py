import pandas as pd
import numpy as np

# Dado de direção do vento no formato string: N, S, E, W.
df = pd.read_csv('../../dados/texto/direcao_vento.txt')

# Remove as linhas duplicadas e retorna apenas o índice e a direção do vento da primeira ocorrência.
# Exemplo: NNE apresenta 3 repetições: índice 49, 84 e 205, porém o resultado será:
# 49 NNE, ou seja, retorna o primeiro índice da série repetida, isto é, o 49.
# subset representa a coluna que se deseja excluir as linhas duplicadas.
direcao_duplicada = df.drop_duplicates(subset = 'Direção')

print(direcao_duplicada)