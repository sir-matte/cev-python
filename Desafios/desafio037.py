# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
# de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Digite um número inteiro: '))
print('''\033[33mEscolha a opção abaixo para converter
-------------------------------------
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL
-------------------------------------''')
o = int(input('INSIRA A OPÇÃO:\033[m '))
if o == 1:
    print('{} convertido para BINÁRIO é {:b}'.format(n, n))
elif o == 2:
    print('{} convertido para OCTAL é {:o}'.format(n, n))
elif o == 3:
    print('{} convertido para HEXADECIMAL é {:x}'.format(n, n))
else:
    print('\033[1;4;31mOPÇÃO INVÁLIDA')

