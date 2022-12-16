# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(n, g):
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


n = str(input('Nome do jogador: ')).strip().title()
g = str(input('Numero de gols: ')).strip()
if n in '':
    n = '<desconhecido>'
if g.isnumeric():
    g = int(g)
else:
    g = 0
ficha(n, g)
