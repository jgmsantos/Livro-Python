nome = 'Egua'  # Variável global.

def diz_egua():
    nome = 'Mano'  # Variável local.
    return f'{nome}! Não acredito!'

print(diz_egua())  # Mano! Não acredito!