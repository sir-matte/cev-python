# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print('''\033[1;32m  ALISTAMENTO MILITAR
-----------------------''')
an = int(input('Informe o ano de nascimento: '))
t = date.today().year - an
if t < 18:
    print('''\033[4;33mVOCÊ AINDA VAI PRECISAR SE ALISTAR
\033[0;33mFalta {} ano(s) para a idade necessária'''.format(18 - t))
elif t > 18:
    print('''\033[1;4;33mVOCÊ NÃO PRECISA MAIS SE ALISTAR
\033[0;33mJá passou {} ano(s) do seu alistamento'''.format(t - 18))
else:
    print('''\033[1;31;4mALISTE-SE JÁ!
\033[0;31;1mEstá na hora do seu alistamento''')