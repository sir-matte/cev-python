# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

l = []
print('\033[1;36m=======================\nCINCO VALORES NUMÉRICOS\n=======================\033[m')
for c in range(0, 5):
    n = int(input('\033[0;33mDigite um número: '))
    if c == 0 or n > l[-1]:
        l.append(n)
        print(f'Número {n} adicionado ao final da lista...')
    else:
        p = 0
        while p < len(l):
            if n <= l[p]:
                l.insert(p, n)
                print(f'Número {n} adicionado na posição {p}')
                break
            p += 1
    print('\033[32m*-' * 30)
print(l)

