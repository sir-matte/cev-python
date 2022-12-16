# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = math.sqrt((co ** 2) + (ca ** 2))
hi = math.hypot(co, ca)
print('A hipotenusa é = {:.2f}\nA hipotenusa é = {:.2f}'.format(h, hi))