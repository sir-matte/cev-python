# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

print('\033[1;35m ÍNDICE DE MASSA CORPORAL\n--------------------------\033[0;34m')
p = float(input('Informe o peso (kg): '))
a = float(input('Informe a altura (m): '))
imc = p / a ** 2
if imc < 18.5:
    print('\033[31m{:.1f} = ABAIXO DO PESO'.format(imc))
elif 18.5 <= imc < 25:
    print('\033[32m{:.1f} = PESO IDEAL'.format(imc))
elif 25 <= imc < 30:
    print('\033[33m{:.1f} = SOBREPESO'.format(imc))
elif 30 <= imc < 40:
    print('\033[31m{:.1f} = OBESIDADE'.format(imc))
else:
    print('\033[31m{:.1f} = OBESIDADE MÓRBIDA'.format(imc))