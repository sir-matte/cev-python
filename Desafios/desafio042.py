# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

print('-=' * 13)
print('Vamos formar um triângulo')
print('=-' * 13)
r1 = float(input('Informe o valor do primeiro lado: '))
r2 = float(input('Informe o valor do segundo lado: '))
r3 = float(input('Informe o valor do terceiro lado: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('O triângulo formado será ', end=(''))
    if r1 == r2 and r2 == r3:
        print('EQUILÁTERO')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r1 == r3 != r2:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('\033[31mIMPOSSÍVEL FORMAR UM TRIÂNGULO')