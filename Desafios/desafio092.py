# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar

from datetime import date
c = {}
c['Nome'] = str(input('Nome: ')).strip().title()
c['Ano'] = int(input('Ano de nascimento: '))
c['Idade'] = date.today().year - c['Ano']
c['CTPS'] = int(input('Nº carteira de trabalho [0 = não tem]: '))
del c['Ano']
if c['CTPS'] == 0:
    print('=' * 40)
    for k, v in c.items():
        print(f'  - {k} = {v}')
else:
    c['Contratação'] = int(input('Ano de contratação: '))
    c['Salário'] = float(input('Salário: R$ '))
    c['Aposentadoria'] = c['Idade'] + 35
    print('=' * 40)
    for k, v in c.items():
        print(f'  - {k} = {v}')
