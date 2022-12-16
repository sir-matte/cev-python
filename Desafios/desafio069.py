# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

m18 = hc = mm20 = 0
while True:
    print('''\033[1;36m~~~~~~~~~~~~~~~~~~~~~
 CADASTRO DE PESSOAS
~~~~~~~~~~~~~~~~~~~~~\033[0;34m''')
    i = int(input('Idade: '))
    s = ' '
    while s not in 'MmFf':
        s = str(input('Sexo [M/F]: ')).strip()[0]
    if i > 18:
        m18 += 1
    if s in 'Mm':
        hc += 1
    if s in 'Ff' and i < 20:
        mm20 += 1
    o = ' '
    while o not in 'SsNn':
        o = str(input('\033[35mQuer continuar?[S/N]: ')).strip()[0]
    if o in 'Nn':
        print('\033[1;33mCADASTRO FINALIZADO!\033[m')
        break
print('\033[1;36m=====================\033[m')
print(f'''\033[33mPessoas com mais de 18 anos: [{m18}]
Homens cadastrados: [{hc}]
Mulheres com menos de 20 anos: [{mm20}]''')
