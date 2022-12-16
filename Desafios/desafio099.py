# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep


def maior(* n):
    m = 0
    print('-==-' * 10)
    print('Analisando os valores passados...')
    sleep(.4)
    for c in range(0, len(n)):
        print(n[c], end=' ')
        sleep(.4)
        if c == 0:
            m = n[c]
        if m < n[c]:
            m = n[c]
    print(f'\n- Foram informados {len(n)} valores ao todo.')
    sleep(.4)
    print(f'- O maior valor informado foi {m}.')


maior(10, 5, 7, 2, 15)
maior(5, 3, 7)
maior(8, 4)
maior(46)
maior()
