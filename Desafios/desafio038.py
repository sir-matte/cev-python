# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

print('\033[1;34mDigite dois números inteiros para comparação')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
print('-------------------\033[0;32m')
if n1 > n2:
    print('O PRIMEIRO número é maior que o segundo!')
elif n2 > n1:
    print('O SEGUNDO número é maior que o primeiro!')
else:
    print('Os números são IGUAIS!')
