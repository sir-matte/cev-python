# Crie um programa que leia o nome de uma cidade, diga se ela começa ou não com o nome “SANTO”.

#MINHA RESOLUÇÃO 1
c = input('Digite o nome de uma cidade: ').title()
if ('Santo' in c):
    print('Esta cidade começa com "Santo"')
else:
    print('Esta cidade não possui "Santo" no nome')
print()

#MINHA RESOLUÇÃO 2
s = c.split()
print('Santo' in s[0])
print()

#RESOLUÇÃO DO PROFESSOR
cid = str(input('Digite a cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')