# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

d = float(input('Qual a distância da viagem em Km? '))
if d <= 200:
    v = d * 0.5
    print('Valor da passagem = R$ {:.2f}'.format(v))
else:
    v = d * 0.45
    print('Valor da passagem = R$ {:.2f}'.format(v))