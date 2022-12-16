# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(n, show=False):
    '''
    -> Calcula o fatorial de um número
    :param n: número a ser calculado
    :param show: (opcional) mostrar ou não a conta.
    :return: valor de um fatorial o número n.
    '''
    f = 1
    for c in range(n, 0, -1):
        if show == True:
            print(c, end=' ')
            if c > 1:
                print(f'x', end=' ')
            if c == 1:
                print(f'=', end=' ')
        f *= c
    return f


print(fatorial(10))
