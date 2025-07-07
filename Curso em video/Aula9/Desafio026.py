frase = str(input('Digite uma frase: ')).strip()
letra = frase.upper().count('A')
primeira = frase.upper().find('A')+1
ultima = frase.upper().rfind('A')
print(f'A letra A apareecu {letra} vezes na frase.\n' f'A primeira letra A apareceu na posição {primeira}.\n' f'A útlima letra A aparece na posição {ultima}.')
