# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda

valor = float(input('Digite um valor: R$ '))
aumentar = moeda.aumentar(valor, 20, True)
diminuir = moeda.diminuir(valor, 20, True)
dobro = moeda.dobro(valor, True)
metade = moeda.metade(valor, True)
print(f'Aumentando 20% = {aumentar}\nDiminuindo 20% = {diminuir}'
      f'\nDobro = {dobro}\nMetade = {metade}')
