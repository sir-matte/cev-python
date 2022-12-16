# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

print('''\033[1;31mMATRIZ 3x3
- - - - - -''', '\033[0;34m')
np = c3 = 0
m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for li in range(0, 3):
    for co in range(0, 3):
        m[li][co] = (int(input(f'{[li, co]}: ')))
        if m[li][co] % 2 == 0:
            np += m[li][co]
        if co == 2:
            c3 += m[li][co]
        if li == 1:
            m2l = max(m[li])
print('- '*10, '\033[36m')
for li in range(0, 3):
    for co in range(0, 3):
        print(f'[{m[li][co]:^5}]', end='')
    print()
print('- '*10, '\033[33m')
print(f'''Soma dos pares: {np}
Soma da terceira coluna: {c3}
Maior número da segunda linha: {m2l}''')
