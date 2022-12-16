# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

n = randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)
print(f'Os números listados foram: ', end='')
for l in n:
    print(l, end=' ')
print(f'\nO maior valor foi {max(n)}\nO menor valor foi {min(n)}')


