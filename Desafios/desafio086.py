# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

print('\033[1;36mMATRIZ 3x3\n', '- '*4, '\033[0;34m')
m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        m[c][l] = int(input(f'{[l, c]}: '))
print('- '*4)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'\033[1;33m[{m[l][c]:^5}]', end='')
    print()
