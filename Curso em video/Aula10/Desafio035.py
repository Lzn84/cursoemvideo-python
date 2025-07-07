print('Analisador de Triângulos')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c > b and c + b > a:
    print('Os segmentos acime PODEM formar um triângulo!')
else:
    print('Os segmento acima NÃO formam um triângulo.')
