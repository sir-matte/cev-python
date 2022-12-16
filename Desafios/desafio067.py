# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

print('\033[1;36m             T A B U A D A\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m')
while True:
    n = int(input('Digite um número (negativo interrompe): '))
    if n < 0:
        print('\033[31mINTERROMPIDO')
        break
    for c in range(1, 11):
        print(f'\033[34m{c} x {n} = \033[32m{c * n}\033[0m')
    print('')
