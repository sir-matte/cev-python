# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

#MINHA RESOLUÇÃO
print('\033[1;36m=*-' * 8)
print('\033[1;36mAPROVAÇÃO DE EMPRÉSTIMO.')
print('\033[1;36m=*-\033[m' * 8)
v = float(input('\033[1;33mValor da casa: R$ '))
s = float(input('Salário do comprador: R$ '))
t = int(input('Quantos anos de financiamento?\033[m '))
p = v / (t * 12)
print('\033[34mA prestação mensal será de R$ {:.2f}'.format(p))
if p > s * 0.3:
    print('\033[1;4;31mEMPRÉSTIMO NEGADO\033[m')
else:
    print('\033[1;4;32mEMPRÉSTIMO APROVADO')