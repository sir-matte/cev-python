n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
so = n1 + n2
sub = n1 - n2
div = n1 / n2
mu = n1 * n2
pot = n1 ** n2
di = n1 // n2
r = n1 % n2
print('a soma é ({})\na subtração é ({})\na divisão é ({:.2f})\na multiplicação é ({})'.format(so, sub,div, mu),end='')
print('\na potência é ({})\na divisão inteira é ({})\no resto da divisão é ({})'.format(pot, di, r))
