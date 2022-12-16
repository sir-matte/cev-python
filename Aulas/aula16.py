# Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python.
# As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura,
# acessíveis por chaves individuais.

lanche = 'pizza', 'pudim', 'suco', 'sorvete', 'batata frita'
for comida in lanche:
    if comida == lanche[2]:
        print(f'Eu vou beber {comida}')
    else:
        print(f'Eu vou comer {comida}')
for cont in range(0, len(lanche)):
    print(lanche[cont])
for pos, comida in enumerate(lanche):
    if comida == 'suco':
        print(f'Eu vou beber {comida} na posição {pos}')
    else:
        print(f'Eu vou comer {comida} na posição {pos}')
print(sorted(lanche))
print('Comi pra caramba!')

a = 2, 5, 4
b = 4, 2, 5, 7
c = a + b
print(c, '\n', c. count(5), '\n', c.index(4, 3))
del(lanche)
