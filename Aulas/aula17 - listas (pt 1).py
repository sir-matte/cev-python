# Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
# As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
# acessíveis por chaves individuais.

num = [2, 6, 1, 3]
num[0] = 9
num.append(25)
num.sort(reverse=True)
num.insert(2, 2)
if 6 in num:
    num.remove(6)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, n in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {n}!')
print('Cheguei ao final da lista.')

a = [6, 4, 1, 2]
b = a[:]
b[2] = 8
print(f'Lista A: {a}\nLista B: {b}')