# Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos seus programas em Python.

#1
n = str(input('Qual seu nome? ')).title()
if 'Gustavo' in n:
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(n))

#2
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
print('Parabéns, você passou!' if m >= 6 else 'Você não passou!')