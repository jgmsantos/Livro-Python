bioma = ['Amazônia', 'Cerrado', 'Pantanal']
nfocos2019 = [6803, 5663, 1532]  # 2019
nfocos2020 = [5803, 4663, 1084]  # 2020

ret = {dados[0]: max(dados[1], dados[2]) for dados in zip(bioma,nfocos2019,nfocos2020)}
print(ret)