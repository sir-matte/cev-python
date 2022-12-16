# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

cont1 = 0
cont2 = 0
print(''' \033[31mINFORME O ANO DE NASCIMENTO
\033[32m-----------------------------\033[m''')
p = ['Primeira', 'Segunda', 'Terceira', 'Quarta', 'Quinta', 'Sexta', 'Sétima']
for c in range(0, 7):
    a = int(input('{} pessoa: '.format(p[c])))
    if date.today().year - a < 18:
        cont1 += 1
    else:
        cont2 += 1
print('Destas 7 pessoas, {} delas não atingiram a maioridade e {} já são maiores.'.format(cont1, cont2))