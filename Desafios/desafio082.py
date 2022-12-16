# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

print('\033[1;36mLISTAS PAR E ÍMPAR')
print('*-'*30, '\033[0;33m')
l = [] #lista
lp = [] #lista par
li = [] #lista ímpar
while True:
    n = int(input('Digite um número: '))
    l.append(n)
    o = ' '
    if n % 2 == 0:
        lp.append(n)
    else:
        li.append(n)
    while o not in 'SsNn':
        o = str(input('Quer continuar? [S/N]: ')).strip()[0]
    if o in 'Nn':
        print('\033[31mListas finalizadas!')
        break
print('\033[35m-*'*30)
print(f'''Foram digitados os números {l}
Números pares {lp}
Números ímpares {li}''')
