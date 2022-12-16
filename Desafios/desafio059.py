# Crie um programa que leia dois valores e mostre um interface na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = float(input('\033[32mDigite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
o = 0
while o != 5:
    print('''-=-=-=-=-=-=-=-=-=-=--=-=-
\033[36;4;1mESCOLHA SUA OPÇÃO A SEGUIR
\033[0;34m[ 1 ] SOMAR        [ 2 ] MULTIPLICAR
\033[33m[ 3 ] MAIOR        [ 4 ] NOVOS NÚMEROS
\033[31m[ 5 ] SAIR DO PROGRAMA\033[0;35m''')
    o = int(input('→ '))
    if o == 1:
        print('Soma = ', n1 + n2)
    if o == 2:
        print('Multiplicação = ', n1 * n2)
    if o == 3:
        print('Número maior = ', max(n1, n2))
    if o == 4:
        n1 = float(input('\033[32mDigite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
print('FIM')