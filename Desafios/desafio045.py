# Crie um programa que faça o computador jogar Jokenpô com você.

#MINHA RESOLUÇÃO
import random
import time

print('\033[31;1m VAMOS JOGAR JOKENPO\n---------------------\033[0;32m')
print('''[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
o = int(input('ESCOLHA A OPÇÃO: '))
c = random.randint(1, 3)
if 0 < o < 4:
    print('PREPARE-SE...')
    print('\033[34mJO'), time.sleep(0.6)
    print('KEN'), time.sleep(0.8)
    print('PO'), time.sleep(0.5)
    print('\033[35m--------------------------')

    if o == 1:
        if c == 1:
            print('(você) Pedra x Pedra (pc)\n           \033[33;4mEMPATE')
        elif c == 2:
            print('(você) Pedra x Papel (pc)\n          \033[31;4mDERROTA')
        else:
            print('(você) Pedra x Tesoura (pc)\n           \033[32;4mVITÓRIA')
    elif o == 2:
        if c == 1:
            print('(você) Papel x Pedra (pc)\n            \033[32;4mVITÓRIA')
        elif c == 2:
            print('(você) Papel x Papel (pc)\n            \033[33;4mEMPATE')
        else:
            print('(você) Papel x Tesoura (pc)\n            \033[31;4mDERROTA')
    elif o == 3:
        if c == 1:
            print('(você) Tesoura x Pedra (pc)\n            \033[31;4mDERROTA')
        elif c == 2:
            print('(você) Tesoura x Papel (pc)\n             \033[32;4mVITÓRIA')
        else:
            print('(você) Tesoura x Tesoura (pc)\n            \033[33;4mEMPATE')
else:
    print('\033[31;4mOPÇÃO INVÁLIDA')
print('\033[0m')

#RESOLUÇÃO DO PROFESSOR

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print ('JOGADOR VENCE')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')