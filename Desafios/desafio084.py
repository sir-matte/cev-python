# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

l = [] #lista
d = [] #dados
mai = men = 0
print('\033[1;36mNOMES E PESAGENS')
print('-*' * 20, '\033[m')
while True:
    d.append(str(input('\033[32mNome: ')))
    d.append(float(input('Peso: \033[m')))
    if len(l) == 0:
        mai = men = d[1]
    else:
        if d[1] > mai:
            mai = d[1]
        elif d[1] < men:
            men = d[1]
    l.append(d[:])
    d.clear()
    o = ' '
    while o not in 'SsNn':
        o = str(input('\033[33mQuer continuar? [S/N]: \033[m')).strip()[0]
    if o in 'Nn':
        break
print(f'\033[34m{len(l)} pessoas foram cadastradas')
print(f'Maior peso foi de {mai} KGs.\n  Peso de', end=' ')
for p in l:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print(f'\nMenor peso foi {men} KGs.\n   Peso de', end=' ')
for p in l:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')




