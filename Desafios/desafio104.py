# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(msg):
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric() == False:
            print('\033[31mINVÁLIDO. Digite um número inteiro válido.\033[m')
        if n.isnumeric():
            return int(n)


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
