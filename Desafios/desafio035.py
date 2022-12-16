# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-=' * 13)
print('Vamos formar um triângulo')
print('=-' * 13)
r1 = float(input('Informe o valor do primeiro lado: '))
r2 = float(input('Informe o valor do segundo lado: '))
r3 = float(input('Informe o valor do terceiro lado: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Esses valores formam um triângulo')
else:
    print('Esses valores não formam um triângulo')