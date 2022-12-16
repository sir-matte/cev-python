# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

# MINHA RESOLUÇÃO
from calendar import isleap

a = int(input('Informe um ano: '))
print('O ano {} é bissexto'.format(a) if isleap(a) == True else 'O ano {} não é bissexto'.format(a))
print('')

# RESOLUÇÃO DO PROFESSOR

from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
