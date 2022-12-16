# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma
# Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

print('\033[1;35mSequência de Fibonacci\n--------------------\033[0;34m')
nt = int(input('Quantos termos você quer mostrar? '))
c = 3
t1 = 0
t2 = 1
print('{} → {}'.format(t1, t2), end='')
while c <= nt:
    c += 1
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3

