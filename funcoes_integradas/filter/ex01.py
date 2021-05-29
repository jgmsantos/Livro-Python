import statistics

# Lista de valores de tempetura em Kelvin.
temp_celsius = [26.8, 33.2, 15.0, 35.4]

# Calculando a média dos dados utilizando a função mean().
media = statistics.mean(temp_celsius)
print(media)  # 27.6

# Compara os valores de temperatura com a "media", e caso o valor seja 
# maior que a media, armazena o resultado em "valor".
tc_filtrada = filter(lambda valor: valor > media, temp_celsius)
print(list(tc_filtrada))  # [33.2, 35.4]