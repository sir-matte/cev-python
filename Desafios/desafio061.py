# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('''============================
    DEZ TERMOS DE UMA PA
============================''')
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
while c < 10:
    c += 1
    print(t, end=' → ')
    t += r
print('\033[31mACABOU')
