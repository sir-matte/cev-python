# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc

num = float(input('Digite um numero real: '))
int = trunc(num)
print('Esse número na forma inteira é igual a {}'.format(int))
