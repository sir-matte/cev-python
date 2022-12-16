# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

#MINHA RESOLUÇÃO
c = 1
s = 0
q = 0
mai = men = 0
while c > 0:
    q += 1
    c += 1
    n = int(input('\033[33mDigite um número: '))
    s += n
    if q == 1:
        mai = men = n
    else:
        if n > mai:
            mai = n
        elif n < men:
            men = n
    o = str(input('\033[33mQuer incluir mais números? \033[32m[S/N]: '))
    if 'N' and 'n' in o:
        c = 0
    elif 'S' and 's' in o:
        continue
    else:
        print('\033[1;31mResposta inválida')
        break
print('~' * 25)
print('''\033[0;34mVocê digitou {}{}{} números
A média desses números é {}{:.1f}{}
O maior número é {}{}{}
O menor número é {}{}{}'''.format('\033[1;36m', q, '\033[0;34m',
                                  '\033[1;36m', s / q, '\033[0;34m',
                                  '\033[1;36m', mai, '\033[0;34m',
                                  '\033[1;36m', men, '\033[0;34m'))
print('')

#RESOLUÇÃO DO PROFESSOR

resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N]: ')).upper()
média = soma / quant
print(quant, média, maior, menor)