print('\033[36mVamos somar dois números!\033[m')
print()
n1 = int(input('\033[31mDigite um número inteiro:\033[m '))
n2 = int(input('\033[34mDigite outro número inteiro:\033[m '))
s = n1 + n2

print('\033[7mA soma de {} com {} é {}\033[m'.format(n1, n2, s))