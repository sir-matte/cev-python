# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

l = []
while True:
    n = int(input('\033[36mDigite um número: \033[m'))
    if n in l:
        n = 0
        print('\033[31mValor duplicado! Não será adicionado...\033[m')
    else:
        l += [n]
        print('\033[32mValor adicionado...\033[m')
    o = ' '
    while o not in 'SsNn':
        o = str(input('\033[33mDeseja continuar? [S/N]: \033[m')).strip()[0]
    if o in 'Nn':
        break

print(f'\033[34m-----------------------------\nForam informados os números {sorted(l)}')
