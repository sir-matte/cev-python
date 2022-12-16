# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

#MINHA RESOLUÇÃO
n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
n3 = int(input('Informe o terceiro valor: '))
n4 = int(input('Informe o quarto valor: '))
t = n1, n2, n3, n4
print(f'\033[35mVocê digitou os números {t}')
print(f'\033[36mO valor [9] apareceu [{t.count(9)}] vezes')
if 3 in t:
    print(f'O primeiro valor [3] foi digitado na [{t.index(3)+1}ª] posição')
if n1 % 2 == 0 or n2 % 2 == 0 or n3 % 2 == 0 or n4 % 2 == 0:
    print(f'Os números pares foram: ', end='')
    for p in t:
        if p % 2 == 0:
            print(f'[{p}]', end=' ')
print('\n\033[33m')

#RESOLUÇÃO DO PROFESSOR
núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores: {núm}')
print(f'O valor [9] apareceu [{núm.count(9)}] vezes')
if 3 in núm:
    print(f'O primeiro valor [3] foi digitado na [{núm.index(3)+1}ª] posição')
else:
    print('O número [3] não foi digitado')
print(f'Os números pares foram: ', end='')
for p in núm:
    if p % 2 == 0:
        print(f'[{p}]', end=' ')
    else:
        print('Não há números pares')


