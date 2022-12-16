#Escreva um programa que pergunte a quantidade de Km percorridos por um
#carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o
#preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('KMs rodados: '))
d = int(input('Dias alugado: '))
ct = (d * 60) + (km * 0.15)

print('Valor a pagar pelo carro alugado: {:.2f}'.format(ct))