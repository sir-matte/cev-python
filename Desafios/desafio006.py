# CRIE UM ALGORITMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA

n = int(input('\033[7mDigite um número:\033[m '))
d = n * 2
t = n * 3
rq = n ** (1/2)
print('\033[1;36mO dobro é {}\n\033[1;37mO triplo é {}\n\033[1;35mA raiz quadrada é {:.2f}'.format(d,t,rq))