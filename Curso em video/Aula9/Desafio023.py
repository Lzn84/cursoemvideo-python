import math
limite = 9999
numero = int(input('Escolha um número de 0 a 9999 para ser lido e dividido: '))
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10
print(f'Seu número é: {numero} \nAgora vamos dividr ele em quantidade de ordens.'f'\nUnidades:{unidade}.'f'\n Dezenas:{dezena}.'
      f'\n Centenas{centena}.' f'\n Milhares:{milhar}.')
