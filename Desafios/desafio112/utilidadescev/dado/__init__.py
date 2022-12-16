def leiaDinheiro(msg):
    while msg.isnumeric() is False:
        preço = str(input(msg)).replace(',', '.').strip()
        if preço.isnumeric() is False:
            print(f'\033[31mERRO: "{preço}" é um preço inválido!\033[m')
        else:
            return float(preço)

def leiaInt(msg):
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric() == False:
            print('\033[31mERRO: Digite um número inteiro válido!\033[m')
        if n.isnumeric():
            return int(n)