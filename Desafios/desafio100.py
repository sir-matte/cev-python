# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a
# soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    c = 1
    while c <= 5:
        r = randint(0, 10)
        if r not in numeros:
            numeros.append(r)
            c += 1
    for i in numeros:
        sleep(.4)
        print(i, end=' ')
    print()


def somaPar(lista):
    s = 0
    for i in numeros:
        if i % 2 == 0:
            s += i
    print(f'Somando os valores pares de {numeros}, temos {s}')

numeros = []
sorteia(numeros)
somaPar(numeros)
