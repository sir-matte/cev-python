# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(a):
    from datetime import date
    i = date.today().year - a
    print(f'Com {i} anos o voto é', end=' ')
    if 18 > i >= 16 or i >= 65:
        return 'OPCIONAL'
    elif i >= 18:
        return 'OBRIGATÓRIO'
    else:
        return 'NEGADO'


a = int(input('Informe o ano de nascimento: '))
print(voto(a))
