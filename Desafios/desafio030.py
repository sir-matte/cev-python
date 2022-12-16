# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um número inteiro: '))
p = n % 2
print('Esse número é par' if p == 0 else 'Esse número é ímpar')