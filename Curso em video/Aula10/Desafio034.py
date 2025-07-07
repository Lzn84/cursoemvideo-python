valor = float(input('Qual o salário do funcionário? '))
alto = (10 / 100) * valor
baixo = (15 / 100) * valor
if valor > 1250:
    print(f'Seu salário será de {valor + alto}')
else:
    print(f'Seu salário será de {valor + baixo}')
