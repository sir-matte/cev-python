# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('\033[36;4;1mTABUADA\033[0;35m')
n = int(input('Informe o número: '))
for c in range(1, 10):
    print('{} x {} = {}'.format(c, n, c * n))