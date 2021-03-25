def calcula_umidade_relativa(e, es):
    """
    Função que calcula a umidade relativa em % 
    dada as variáveis "e" e "es".
    e = pressão de vapor (hPa).
    es = pressão de saturação do vapor (hPa).
    """
    ur = (e/es) * 100
    return ur
 
 
rh = calcula_umidade_relativa(209, 383)
print(f'O valor da UR é: {rh}%')  # O valor da UR é: 54.56919060052219%

print(calcula_umidade_relativa.__doc__)