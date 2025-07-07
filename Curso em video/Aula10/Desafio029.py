km = int(input('A quantos km seu carro está? '))
multa = (km - 80) * 7
if km >80:
    print(f'MULTADO. Você está acima da velocidade permitida (80km) pague uma multa de R${multa}')
else: print('PERFEITO! Você está dentro do limite de velocidade, se mantenha assim.')
