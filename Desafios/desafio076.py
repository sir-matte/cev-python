# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

l = ('Lápis', 2.50,
     'Caderno', 12.90,
     'Caneta', 3.95,
     'Borracha', 2,
     'Pasta', 15.65,
     'Marca texto', 5.90,
     'Mochila', 109.90,
     'Compasso', 12.70)
print('\033[1;32m=='*20)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('=='*20, '\033[0;33m')
for p in range(0, len(l)):
     if p % 2 == 0:
          print(f'{l[p]:.<30}', end='')
     else:
          print(f'R$ {l[p]:>7.2f}')
