# Lista de valores de tempetura em Kelvin.
temp_kelvin = [300, 280, 350, 315]

# 1) Utilizando a função integrada map com lambda (função sem nome).
tc = map(lambda tk: tk-273.15,temp_kelvin)
# Para visualizar os valores tem que converter map para list.
print(list(tc))  

# 2) Utilizando map com função.
# Definindo a função que converte de Kelvin para Celsius.
def kelvin_to_celsius(tk):
    return tk -273.15

tc = map(kelvin_to_celsius,temp_kelvin)
print(list(tc))