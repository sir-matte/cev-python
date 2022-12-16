# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
# encontram no intervalo de 1 até 500.

print('SOMA DOS MÚLTIPLOS DE TRÊS, DO 1 ao 500')
s = 0
c = 0
for n in range(3, 501, 3):
    i = n % 2
    if i == 1:
        c += 1
        s += n
print('A soma dos {} números é {}'.format(c, s))

