# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

ang = float(input('Informe o ângulo: '))
se = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))

print('Seno = {:.2f}\nCosseno = {:.2f}\nTangente = {:.2f}'.format(se, cos, tg))