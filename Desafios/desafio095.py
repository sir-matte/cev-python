# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

cj = {} #cadastro jogador
t = [] #time
g = [] #gols
while True:
    cj['nome'] = str(input('\033[36mNome do jogador: ')).strip().title()
    p = int(input(f'Quantas partidas {cj["nome"]} jogou? '))
    for c in range(0, p):
        g.append(int(input(f'  Quantos gols na {c+1}ª partida? ')))
    cj['gols'] = g[:]
    cj['total'] = sum(g)
    t.append(cj.copy())
    g.clear()
    o = ' '
    while o not in 'SsNn':
        o = str(input('\033[34mDeseja continuar? [S/N]: ')).strip()[0]
        if o not in 'SsNn':
            print('\033[31mInválido! Tente novamente.')
    if o in 'Nn':
        print('\033[31mFinalizado!')
        print('\033[33m=' * 50)
        break
    print('-' * 40)
print('cód', end='  ')
for i in cj.keys():
    print(f'{i:<20}', end='')
print()
print('=' * 50)
for k, v in enumerate(t):
    print(f'\033[32m{k:>3}', end='  ')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()
print('\033[33m=' * 50)
while True:
    cod = int(input('\033[34mMostrar dados de qual jogador(cód)? [999 para interromper]: '))
    if cod == 999:
        print('\033[31m<< Finalizado >>')
        break
    if cod >= len(t):
        print(f'\033[31mInválido! Tente novamente.')
    else:
        print(f'\033[33m-- LEVANTAMENTO DO JOGADOR {t[cod]["nome"]}')
        for cp, ng in enumerate(t[cod]['gols']): #contador de partidas e numero de gols
            print(f'   \033[32mNa partida {cp+1} fez {ng} gols.')


