# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

#PRIMEIRA RESOLUÇÃO
print('\033[1;36m INFORME AS PESAGENS\n\033[35m---------------------\033[0;33m')
l = []
for c in range(1, 6):
    p = float(input('{}ª pessoa: '.format(c)))
    l += [p]
print('\033[31mMaior peso é {:.1f} Kg\nMenor peso é {:.1f} Kg\033[m'.format(max(l), min(l)))

#SEGUNDA RESOLUÇÃO
menor = 0
maior = 0
for pessoas in range(1, 6):
    peso = float(input('{}ª pessoa: '.format(pessoas)))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('Maior peso é {} kgs, menor peso é {} kgs'.format(maior, menor))