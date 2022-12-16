# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

print('\033[31;1mPREPAREM-SE PARA OS FOGOS!\n    COMEÇANDO EM...\033[0;33m')
for c in range(10, 0 - 1, - 1):
    sleep(1)
    print('         {}'.format(c))
print('    BOOM!! POW!!!!')
