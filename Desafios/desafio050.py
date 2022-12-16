# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

ns = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto']
s = 0
cont = 0
for c in range(0, 6):
    n = int(input('\033[36mInforme o {} número: '.format(ns[c])))
    if n % 2 == 0:
        s += n
        cont += 1
print('\033[35mSoma de todos os {} números pares = {}'.format(cont, s))
