# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

j = {}
g = []
j['Nome'] = str(input('Nome do jogador: ')).strip().title()
p = int(input(f'Quantas partidas {j["Nome"]} jogou? '))
for c in range(0, p):
    g.append(int(input(f'  Quantos gols na {c}ª partida? ')))
j['Gols'] = g
j['Total'] = sum(g)
print('=' * 30)
print(j)
print('=' * 30)
for k, v in j.items():
    print(f'{k} = {v}')
print('=' * 30)
print(f'O jogador {j["Nome"]} jogou {p} partidas')
for c in range(0, p):
    print(f'  => Na partida {c}, fez {g[c]} gols')
print(f'Foi um total de {j["Total"]} gols')
