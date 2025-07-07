n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

print(f'Os valores digitados são: {n1}, {n2}, {n3}.')
if n1 > n2 and n1 > n3:
    print(f'O valor MAIOR é {n1}.')
elif n2 > n1 and n2 > n3:
    print(f'O valor MAIOR é {n2}.')
else: 
    print(f'O valor MAIOR é {n3}.')
if n1 < n2 and n1 < n3:
    print(f'O valor MENOR é {n1}.')
elif n2 < n1 and n2 < n3:
    print(f'O valor MENOR é {n2}.')
else: 
    print(f'O valor MENOR é {n3}.')
