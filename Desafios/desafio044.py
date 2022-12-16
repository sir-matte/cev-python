# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

print(' \033[31;1mLOJA DO MATTE\n---------------\033[0;32m')
v = float(input('Valor das compras:\nR$ '))
print('''\033[0;33mForma de pagamento:
[ 1 ] pix ou dinheiro: 10% de desconto
[ 2 ] débito: 5% de desconto
[ 3 ] crédito 2x: valor sem juros
[ 4 ] crédito 3x: 20% de juros''')
o = int(input('Opção: '))
if 4 >= o >= 1:
    print('\033[34mValor final:')
    if o == 1:
        v = v - (v * 0.1)
        print('R$ {:.2f}'.format(v))
    elif o == 2:
        v = v - (v * 0.05)
        print('R$ {:.2f}'.format(v))
    elif o == 3:
        print('R$ {:.2f}'.format(v))
    elif o == 4:
        v = v + (v * 0.2)
        print('R$ {:.2f}'.format(v))
else:
    print('\033[31;4mOpção Inválida')