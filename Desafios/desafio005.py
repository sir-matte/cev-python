# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E SEU ANTECESSOR

n = int(input('\033[4;41mDigite um número inteiro:\033[m '))
suc = n + 1
ant = n - 1
print('\033[32mO número antecessor a esse é {}\n\033[31mO número sucessor a esse é {}\033[m'.format(ant, suc))