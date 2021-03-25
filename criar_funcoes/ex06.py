def calcula_umidade_relativa(e, es):
    ur = (e/es) * 100
    return ur


rh = calcula_umidade_relativa(209, 383)
print(f'O valor da UR é: {rh}%')  # O valor da UR é: 54.56919060052219%