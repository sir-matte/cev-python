# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Velocidade do carro em Km/h: '))

if v > 80:
    m = (v - 80) * 7
    print('VELOCIDADE EXCEDIDA!\nMULTA = R${:.2f}'.format(m))
else:
    print('Tenha um bom dia! Dirija com segurança!')