x = [1, 30, 5, 8, 2]
#    0   1  2  3  4  <= Posições.

print(x[1:])  # [30, 5, 8, 2]

print(x[::])  # [1, 30, 5, 8, 2] => Todos os elementos da lista.

print(x[:2])  # [1, 30] => Lembrando que o índice 2 não é incluído.

print(x[1:3])  # [30, 5] => Lembrando que o índice 3 não é incluído.

print(x[1::2])  # [30, 8] => Vai do índice 1 até o final com passo 2.

print(x[::2])  # [1, 5, 2] => Vai do índice 0 até o final com passo 2.

print(x[::-2])  # [1, 5, 2] => Vai do índice 0 até o final com passo 2.