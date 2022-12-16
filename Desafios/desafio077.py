# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

lista = ('PYTHON', 'TRABALHO', 'COMPUTADOR', 'TELEVISÃO', 'TECLADO', 'MOUSE', 'NOTEBOOK', 'MESA', 'CADEIRA', 'TAPETE')
for palavras in lista:
    print(f'Vogais na palavra [{palavras}] =', end=' ')
    for c in palavras:
        if c in 'AEIOU':
            print(f'[{c}]', end='')
    print('')
