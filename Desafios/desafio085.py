# Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

print(f'\033[1;36m    -- LISTAS --\n - Pares & Ímpares -')
print('='*21, '\033[0;34m')
l = [[], []]
for c in range(1, 8):
    n = int(input(f'{c}º número: '))
    if n % 2 == 0:
        l[0].append(n)
    else:
        l[1].append(n)
l[0].sort()
l[1].sort()
print(f'\033[31mNúmeros pares: {l[0]}\n\033[33mNúmeros ímpares: {l[1]}')
