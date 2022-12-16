# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

b = {}
b['Nome'] = str(input('\033[1;34mNome do aluno: ')).title()
b['Média'] = float(input(f'Média de {b["Nome"]}: \033[0m'))
if b['Média'] >= 7:
    b['Situação'] = '\033[32mAprovado'
elif b['Média'] < 5:
    b['Situação'] = '\033[31mReprovado'
else:
    b['Situação'] = '\033[33mRecuperação'
print('\033[34m=' * 25)
for k, v in b.items():
    print(f'''\033[36m- {k} =\033[m {v}''')