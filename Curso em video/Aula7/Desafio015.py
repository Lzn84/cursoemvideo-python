# valor da diaria 60 - valor dos km 0,15 - formúla
dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram rodados? '))
x = dias * 60
y = km * 0.15
preço = x + y
# total na tela
print('O valor do aluguel do carro ficou R${}.'.format(preço))
