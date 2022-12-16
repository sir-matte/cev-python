# ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS

n = float(input('Digite um número em metros: '))
print('Centímetros = {:.0f}\nMilímetros = {:.0f}\nQuilômetros = {:.3f}'.format(n*100,n*1000,n/1000))
