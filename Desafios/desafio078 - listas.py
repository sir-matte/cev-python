# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

n = []
for c in range(0, 5):
    n.append(int(input(f'Digite o número da posição {c}: ')))
print('='*30)
print(f'Você digitou os números \033[36m{n}\033[m')
print(f'O maior número digitado foi \033[36m[{max(n)}]\033[m nas posições ', end='')
for p, v in enumerate(n):
    if v == max(n):
        print(f'\033[36m{p}\033[m', end='...')
print(f'\nO menor número digitado foi \033[36m[{min(n)}]\033[m nas posições ', end='')
for p, v in enumerate(n):
    if v == min(n):
        print(f'\033[36m{p}\033[m', end='...')
