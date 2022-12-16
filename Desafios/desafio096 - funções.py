# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um
# terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l, c):
    a = l * c
    print(f'A área de um terreno {l} x {c} é de {a}m².')


print(' CONTROLE DE TERRENOS')
print('-' * 25)
area(l=float(input('Largura (m): ')), c=float(input('Comprimento (m): ')))

''' >>RESOLUÇÃO DO PROFESSOR<<
def area(l, c):
        a = l * c
        print(f'A área de um terreno {l} x {c} é de {a}m².')
        
        
print(' CONTROLE DE TERRENOS')
print('-' * 25)
l = float(input('Largura (m): ')
c = float(input('Comprimento (m): ')
area(l, c)
'''