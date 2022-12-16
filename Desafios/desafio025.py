# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

#MINHA RESOLUÇÃO 1
n = str(input('Digite o nome: ')).upper()
if('SILVA' in n):
    print('Esse nome possui "Silva"')
else:
    print('Esse nome não possui "Silva"')
print()

#MINHA RESOLUÇÃO 2
print('SILVA' in n)

