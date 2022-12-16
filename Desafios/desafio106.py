# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
# Importante: use cores.
c = ['\033[m', '\033[1;30;41m', '\033[1;30;43m', '\033[1;30;44m', '\033[7m']


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


def ajuda(com):
    help(com)

# Programa Principal
comando = ''


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Biblioteca ou função > '))
    if comando.upper().strip() == 'FIM':
        titulo('ATÉ LOGO!', 1)
        break
    else:
        titulo(f"Acessando o manual do comando '{comando}'", 3)
        print(c[4])
        ajuda(comando)
        print(c[0], end='')
