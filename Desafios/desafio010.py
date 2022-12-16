# CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA
# E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR - CONSIDERE US$1,00 = R$ 5,06

r = float(input('Quantos reais você tem? '))
d = r / 5.06

print('Você pode comprar {:.2f} dólares!'.format(d))
