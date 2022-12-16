# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%

s = float(input('Informe o salário do funcionário: '))
if s > 1250:
    s = s * 0.1 + s
    print('Novo salário com aumento de 10% = R$ {:.2f}'.format(s))
else:
    s = s * 0.15 + s
    print('Novo salário com aumento de 15% = R$ {:.2f}'.format(s))