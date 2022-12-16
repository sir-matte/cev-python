# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números
# como um valor monetário formatado.

import moeda

valor = float(input('Digite um valor: R$ '))
aumentar = moeda.moeda(moeda.aumentar(valor, 20))
diminuir = moeda.moeda(moeda.diminuir(valor, 20))
dobro = moeda.moeda(moeda.dobro(valor))
metade = moeda.moeda(moeda.metade(valor))
print(f'Aumentando 20% = {aumentar}\nDiminuindo 20% = R$ {diminuir}'
      f'\nDobro = R$ {dobro}\nMetade = R$ {metade}')
