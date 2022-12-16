# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print('''============================
    DEZ TERMOS DE UMA PA
============================''')
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(0, 10):
    print(t, end='\033[35m → ')
    t += r
print('\033[31mACABOU')