# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('=' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        c = i
        while c <= f:
            sleep(0.5)
            print(f'{c}', end=' ')
            c += p
        print('FIM!')
    else:
        c = i
        while c >= f:
            sleep(0.5)
            print(f'{c}', end=' ')
            c -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('=' * 30)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)








#SOLUÇÃO COM FOR(ERRADA!)
'''
def contador(i, f, p):
    print('=' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    for c in range(i, f+1, p):
        sleep(0.5)
        print(c, end=' ')
    print('FIM!')


contador(1, 10, 1)
contador(11, 0, -2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
'''