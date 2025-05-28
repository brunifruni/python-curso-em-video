import random
from random import randint
print('-'*10, 'Sorteador', '-'*10)
n1 = int(input("Digite um número (0-5): "))
n = random.randint(0,5)
if n1 == n:
    print(f'Parabéns você acertou! O número sorteado foi {n}')
else:
    print(f'Você errou! O número sorteado foi {n}')