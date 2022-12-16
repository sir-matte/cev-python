# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Informe um número inteiro: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        cont += 1
        print('\033[31m', end='')
    else:
        print('\033[m', end='')
    print('{} '.format(c), end='')
print('\033[0m\nO número {} foi divisível {} vezes'.format(n, cont))
if cont > 2:
    print('Portanto não é um número primo')
else:
    print('Portanto é um número primo')
