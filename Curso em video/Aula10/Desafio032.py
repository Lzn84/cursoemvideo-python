from datetime import date
ano = int(input('Qual ano você quer analisar? Insira 0 para analisar o ano atual. '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else: print(F'O ano {ano} NÃO é BISSEXTO')
