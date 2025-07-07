import random
sorteio = random.choice([0, 1, 2, 3, 4, 5])
user = int(input('Eu pensei um número entre 0 a 5... Tente advinhar qual foi!'))
if sorteio == user:
    print(f'Inacreditável, você ACERTOU!! eu pensei {sorteio}')
else: print(f'Poxa, não foi dessa vez... O número era {sorteio}')
