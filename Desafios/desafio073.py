# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Internacional.

t = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'América-MG',
     'Fortaleza', 'Botafogo', 'Santos', 'Goiás', 'São Paulo', 'Bragantino', 'Coritiba', 'Ceará', 'Cuiabá',
     'Avaí', 'Atlético-GO', 'Juventude')
print('\033[1;32mTabela Brasileirão Série A - 03/10/22\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=\033[0;33m')
print(f'{t}\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=\033[34m')
print(f'Os 5 primeiros colocados são: {t[0:5]}\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=\033[35m')
print(f'Os últimos 4 colocados são: {t[-4:]}\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=\033[36m')
print(f'Times em ordem alfabética: {sorted(t)}\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=\033[31m')
print(f'O Internacional está na {t.index("Internacional")+1}ª posição')



