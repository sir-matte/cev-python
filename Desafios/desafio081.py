# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

print('\033[1;32mLEITOR DE NÚMEROS')
print('*-'*15)
l = []
while True:
    l.append(int(input('\033[0;33mDigite um número: ')))
    o = ' '
    while o not in 'SsNn':
        o = str(input('Quer continuar? [S/N]: ')).strip()[0]
    if o in 'Nn':
        print('\033[31mLista finalizada!')
        break
l.sort(reverse=True)
print('\033[35m*-'*15,
f'''\nForam digitados [{len(l)}] números.
Lista em ordem decrescente: {l}''')
if 5 in l:
    print('O número [5] está na lista!')
else:
    print('O número [5] não está na lista!')