# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date

print('\033[36;4;1mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[0;34m')
an = int(input('Informe o ano de nascimento do atleta: '))
i = date.today().year - an
print('\033[35mO atleta tem {} anos\033[1m'.format(i))
if i <= 9:
    print('CATEGORIA MIRIM')
elif 9 < i <= 14:
    print('CATEGORIA INFANTIL')
elif 14 < i <= 19:
    print('CATEGORIA JÚNIOR')
elif 19 < i <= 25:
    print('CATEGORIA SÊNIOR')
else:
    print('CATEGORIA MASTER')