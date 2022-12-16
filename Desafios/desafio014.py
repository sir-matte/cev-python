# ESCREVA UM PROGRAMA QUE CONVERTA UMA TEMPERATURA DIGITADA EM ºC E CONVERTA PARA ºF.

c = float(input('Digite a temperatura em ºC: '))
f = c * 1.8 + 32

print('{:.0f}ºC é equivalente a {:.1f}ºF'.format(c, f))