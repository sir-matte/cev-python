# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

#MINHA RESOLUÇÃO
from random import randint
from time import sleep
print('\033[1;32m=$='*7)
print(' PALPITES MEGA SENA')
print('=$='*7, '\033[0;33m')
ns = int(input('Quantos palpites serão gerados? '))
l = []
print(f'\033[1;32m=$=$= Sorteando {ns} palpites =$=$=\033[m')
for q in range(0, ns):
    sleep(1)
    print(f'\033[33mJogo {q+1}: \033[m')
    for n in range(1, 7):
        l = randint(1, 60)
        print(f'\033[32m[{l}]\033[m', end='')
    print()
print()

#RESOLUÇÃO DO PROFESSOR

lista = list()
jogos = list()
print('-' * 30)
print('       JOGA NA MEGA SENA         ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'SORTEANDO {quant} JOGOS')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)