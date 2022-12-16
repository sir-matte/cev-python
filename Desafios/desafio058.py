#  Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
#  Só que agora o jogador vai tentar adivinhar até acertar,
#  mostrando no final quantos palpites foram necessários para vencer.

#MINHA RESOLUÇÃO
from random import randint
pc = randint(0, 10)
c = 1
print('\033[36;1mTENTE ADIVINHAR UM NÚMERO DE 0 A 10\n-----------------\033[0;34m')
p = int(input('Palpite: '))
while p != pc:
    if p < pc:
        p = int(input('↑\n\nNovo palpite: '))
        c += 1
    if p > pc:
        p = int(input('↓\n\nNovo palpite: '))
        c += 1
print('\n\033[1;4;32mCERTA RESPOSTA\n\033[0;33mNúmero {}\nTentativas: {}'.format(pc, c))
print('\n\n')

#RESOLUÇÃO DO PROFESSOR
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente.')
        elif jogador > computador:
            print('Menos... Tente novamente.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
