# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input('\033[1;4;36mInforme um número inteiro:\033[0;35m '))
print('Fatorial de {}\n\033[34m{}! = '.format(n, n), end='')
f = 1
c = n
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('\033[1;4;31m{}\033[0;31m  FIM'.format(f))