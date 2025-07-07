km = int(input('De quantos km será sua viagem? '))
rapida = 0.50 * km
longa = 0.45 * km
if km >=200:
    print(f'Sua passagem fica no total de R${longa:.2f}')
else: print(f'Sua passagem fica no total de R${rapida:.2f}')