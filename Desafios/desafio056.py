# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

si = 0 #soma das idades
ima = 0 #idade maior
hv = '' #homem velho
m = 0   #mulheres
for p in range(1, 5):
    print('\033[1;32m----\033[34m {}ª PESSOA \033[32m----\033[0;35m'.format(p))
    n = str(input('Nome: '))
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).upper().strip()
    si += i
    if i > ima and s == 'M':
        ima = i
        hv = n
    if i < 20 and s == 'F':
        m += 1
print('''\033[33;4m\nESTE PROGRAMA LEU AS SEGUINTES INFORMAÇÕES:\033[0;36m
A média idade é {:.0f} anos
O homem mais velho é o {}
Possue {} mulheres com menos de 20 anos'''.format(si / 4, hv, m))

