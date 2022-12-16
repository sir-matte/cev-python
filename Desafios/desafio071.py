# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o
# programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

c = 50
tc = 0
print('\033[1;32m$' * 30)
print('\033[33m{:^30}\033[32m'.format('BANCO ALEGRE'))
print('$' * 30, '\033[0;36m')
s = int(input('\nValor para saque\nR$ '))
t = s
while True:
    if t >= c:
        tc += 1
        t -= c
    else:
        if tc > 0:
            print(f'{tc} cédulas de {c}')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        tc = 0
        if t == 0:
            break
