# Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python,
# o uso de docstrings para documentar nossas funções, argumentos opcionais para dar mais dinamismo em funções Python,
# escopo de variáveis e retorno de resultados.

#help(print)
#print(input.__doc__)


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par')
else:
    print('Não é par')
