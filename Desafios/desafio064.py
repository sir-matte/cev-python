# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

c = 1
q = s = 0
while c > 0:
    c += 1
    q += 1
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        s += n
    else:
        c = 0
print('Números digitados = {}\nSoma entre os números = {}'.format(q - 1, s))
