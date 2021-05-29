bioma = ['Amazônia', 'Cerrado', 'Pantanal']
numero_focos_queimadas = [6803, 5663, 1684]

# bioma = bioma =          ['Amazônia', 'Cerrado', 'Pantanal']
# numero_focos_queimadas = [6803      , 5663     , 1684]
# Índice                     0          1          2
 
ret = zip(bioma,numero_focos_queimadas)
print(list(ret))  # [('Amazônia', 6803), ('Cerrado', 5663), ('Pantanal', 1684)]