# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
# e mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’)
# Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~

def escreva(frase):
    tam = len(frase) + 4
    print('~' * tam)
    print(f'  {frase}')
    print('~' * tam)


escreva('Harry Potter')
escreva('Harry')
escreva('Harry Potter e o Prisioneiro de Azkaban')