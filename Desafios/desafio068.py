# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

v = 0
print('''\033[1;36m  VAMOS JOGAR PAR OU ÍMPAR!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m''')
while True:
    pc = randint(0, 10)
    pi = str(input('\033[34mPar ou ímpar? [P/I]: ')).strip()
    while pi not in 'PpIi':
        print('\033[31mINCORRETO!\033[m')
        pi = str(input('\033[34mPar ou ímpar? [P/I]: ')).strip()
    n = int(input('Número: '))
    s = (n + pc) % 2
    print('DEU PAR!' if s == 0 else 'DEU ÍMPAR!')
    print(f'\033[34mNúmero do PC: [{pc}]')
    if pi in 'Pp' and s == 0:
        print('\033[32mVITÓRIA!\033[m')
        v += 1
    elif pi in 'Ii' and s == 1:
        print('\033[32mVITÓRIA!\033[m')
        v += 1
    else:
        print('\033[31mDERROTA!\033[m')
        break
print(f'\033[33mNúmero de vitórias consecutivas [{v}]')
