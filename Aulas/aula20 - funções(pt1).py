# Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python.
# Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python.
# Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A e B é {s}')
    print('-' * 20)


soma(5, 10)
soma(b=3, a=3)
soma(1, 1)


def contador(* num):
    tam = len(num)
    print(f'Valores {num} e ao todo {tam} números')
    for valor in num:
        print(f'{valor} ', end='')
    print('fim!')
    print('-' * 30)


contador(2, 1, 4)
contador(1, 5, 8, 9, 22)
contador(3, 1)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print('-' * 30)


valores = [4, 2, 4, 65, 12]
dobra(valores)
print(valores)
