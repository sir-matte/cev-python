# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('''\033[1;36m
| SUPER SHOP |
| [Produtos] |''')
tg = qpc = pb = npb = cont = 0
while True:
    print('\033[0;34m--------------')
    p = str(input('Produto: ')).strip()
    v = float(input('Preço: R$ '))
    tg += v
    cont += 1
    if cont == 1:
        pb = v
    else:
        if v < pb:
            pb = v
            npb = p
    if v > 1000:
        qpc += 1
    o = ' '
    while o not in 'SsNn':
        o = str(input('\033[35mDeseja continuar? [S/N]: ')).strip()[0]
    if o in 'Nn':
        print('\033----------------\n\033[31mLISTA FINALIZADA')
        break
print(f'''\033[33m================
Total gasto = R$ {tg:.2f}
Produtos que custam mais de R$ 1000,00 = [{qpc}]
Produto mais barato = [{npb}]''')
