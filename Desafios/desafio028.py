# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

#MINHA RESOLUÇÃO
import random
ns = [0, 1, 2, 3, 4, 5]
ne = random.choice(ns)
n = int(input('Digite um número de 0 a 5: '))
print('Número sorteado:', ne)
print('Vencedor! Parabéns!' if n == ne else 'Perdeu! Tente denovo!')

#RESOLUÇÃO DO PROFESSOR
from random import randint
from time import sleep
computador = randint(0, 5)
print('-=' * 30)
print('VOU PENSAR EM UM NÚMERO ENTRE 0 E 5. TENTE ADIVINHAR...')
print('=-' * 30)
jogador = int(input('Em que número pensei? '))
print('PROCESSANDO')
print('.'), sleep(0.5)
print('.'), sleep(0.5)
print('.'), sleep(0.5)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {} !'.format(computador, jogador))
