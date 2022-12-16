# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter


j = {'P1': randint(1, 6),
     'P2': randint(1, 6),
     'P3': randint(1, 6),
     'P4': randint(1, 6)}
r = []
print('JOGO DE DADOS')
print('-' * 20)
print('Jogando os dados...\n')
for k, v in j.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
r = sorted(j.items(), key=itemgetter(1), reverse=True)
print('=' * 25)
print('== RANKING DOS PLAYERS ==')
for i, v in enumerate(r):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
