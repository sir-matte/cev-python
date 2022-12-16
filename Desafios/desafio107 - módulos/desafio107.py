# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

valor = float(input('Digite um valor: R$ '))
aumentar = moeda.aumentar(valor, 20)
diminuir = moeda.diminuir(valor, 20)
dobro = moeda.dobro(valor)
metade = moeda.metade(valor)
print(f'Aumentando 20% = R$ {aumentar:.2f}\nDiminuindo 20% = R$ {diminuir:.2f}'
      f'\nDobro = R$ {dobro:.2f}\nMetade = R$ {metade:.2f}')
