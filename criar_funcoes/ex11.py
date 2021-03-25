def diz_egua():
    """Função que retorna uma expressão paraense."""
    nome = 'Egua'  # Variável local.
    return f'{nome}! Não acredito!'

print(diz_egua())  # Egua! Não acredito!

print(help(diz_egua))

# Utilizando a propriedade especial __doc__.
print(diz_egua.__doc__)  # Função que retorna uma expressão paraense.