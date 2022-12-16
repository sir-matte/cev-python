# FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE
# SEU NOVO PREÇO, COM 5% DE DESCONTO

p = float(input('Digite o preço do produto: '))
pd = p - (p * 0.05)

print('Valor com 5% de desconto = {:.2f}'.format(pd))