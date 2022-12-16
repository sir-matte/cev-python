def aumentar(preço=0, taxa=0, formato=True):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=True):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=True):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=True):
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda} {preço:.2f}'.replace('.', ',')


def resumo(preço=0, a=0, r=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado:\t{moeda(preço)}')
    print(f'{a}% de aumento:\t\t{aumentar(preço, a)}')
    print(f'{r}% de redução:\t\t{diminuir(preço, r)}')
    print(f'Dobro do preço:\t\t{dobro(preço)}')
    print(f'Metade do preço:\t{metade(preço)}')
    print('-' * 30)
