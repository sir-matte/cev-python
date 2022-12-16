# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada
# aluno individualmente.

print('\033[1;36m BOLETINS')
print('-' * 10)
l = []
d = []
m = []
while True:
    d.append(str(input('\033[0;33mNome do aluno: ')).title())
    d.append(float(input('Nota 1: ')))
    d.append(float(input('Nota 2: ')))
    m.append((d[1] + d[2]) / 2)
    l.append(d[:])
    d.clear()
    o = ' '
    while o not in 'SsNn':
        o = str(input('\033[32mQuer continuar? [S/N]: ')).strip()[0]
    if o in 'Nn':
        break
print('=' * 32)
print(f' \033[1;34m{"Nº":<5}{"NOME":<20}{"MÉDIA":>5}')
print('-' * 32)
for i, a in enumerate(l):
    print(f' \033[m{i:<5}{a[0]:<20}{m[i]:>5.1f}')
print('\033[1;34m-' * 32)
while True:
    o = int(input(f'\033[0;35mMostrar notas de qual aluno (Nº)?\n[{i+1}+ para finalizar]: '))
    if o > i:
        print('\033[1;31mFinalizado!')
        break
    else:
        print(f'\033[34mNotas de \033[0m{l[o][0]}\033[34m = \033[0m{[l[o][1],l[o][2]]}')



