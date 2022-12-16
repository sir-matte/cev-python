# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

m = 0
d = {}
l = []
while True:
    print('\033[1;36m-' * 21)
    print(' -= NOVO CADASTRO =-\033[0m')
    d['nome'] = str(input('\033[34mNome: ')).strip().title()
    d['sexo'] = ' '
    while d['sexo'] not in 'MmFf':
        d['sexo'] = str(input('\033[34mSexo [M/F]: ')).strip()[0]
        if d['sexo'] not in 'MmFf':
            print('\033[31mInválido! Tente novamente\033[m')
    d['idade'] = int(input('\033[34mIdade: '))
    m += d['idade']
    l.append(d.copy())
    print('\033[32mCadastrado com sucesso!\033[m')
    o = ' '
    while o not in 'SsNn':
        o = str(input('\033[0;33mDeseja continuar? [S/N]: \033[m')).strip()[0]
        if o not in 'SsNn':
            print('\033[31mInválido! Tente novamente\033[m')
    if o in 'Nn':
        print('\033[31mFinalizado!')
        break
m = m / len(l)
print('\033[1;36m-' * 40)
print(f'''\033[0;35mA) Ao todo temos {len(l)} pessoas cadastradas.
B) A média de idade é de {m:.1f}
C) As mulheres cadastradas foram:''', end=' ')
for i in l:
    if i['sexo'] in 'Ff':
        print(i['nome'], end='; ')
print('\nD) Pessoas acima da média de idade:')
for i in l:
    if i['idade'] > m:
        print('     ', end='')
        for k, v in i.items():
            print(f'{k} = {v}', end='; ')
        print()
print('\033[1;36m-' * 40)
