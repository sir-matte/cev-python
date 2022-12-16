# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número
# de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(i):
    while True:
        try:
            n = int(input(i))
        except ValueError:
            print('\033[31mINVÁLIDO. Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não informar os dados!\033[m')
            return 'nulo'
        else:
            return n


def leiaFloat(f):
    while True:
        try:
            n = str(input(f)).strip().replace(',', '.')
            n = float(n)
        except ValueError:
            print('\033[31mINVÁLIDO. Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não informar os dados!\033[m')
            return 'nulo'
        else:
            return n


i = leiaInt('Digite um Inteiro: ')
f = leiaFloat('Digite um Real: ')
print(f'O valor inteiro foi {i} e o valor real foi {f}')
