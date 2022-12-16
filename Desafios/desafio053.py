# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

#MINHA RESOLUÇÃO SEM FOR
#f = str(input('Digite uma frase: ')).replace(' ', '').upper()
#ff = f[::-1]
#print('A frase {} invertida fica {}'.format(f, ff))
#if f == ff:
#    print('Portanto ela é um palíndromo')
#else:
#    print('Portanto ela não é palíndromo')

#RESOLUÇÃO COM FOR
f = str(input('Digite uma frase: ')).upper().split()
j = ''.join(f)
i = ''
for l in range(len(j) - 1, -1, -1):
    i += j[l]
print('{} no inverso fica {}'.format(j, i))
if j == i:
    print('Portanto é um palíndromo')
else:
    print('Portanto não é um palíndromo')