# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo sem considerar espaços.
# – Quantas letras tem o primeiro nome.

#MINHA RESOLUÇÃO
n = input('Digite o nome completo: ')
nr = n.replace(' ', '')
ns = n.split()
print('Maiúsculas: {0}\nMinúsculas: {1}\nTotal de letras: {2}\nLetras do primeiro nome: {3}'
      .format(n.upper(), n.lower(), nr.count('', 1, 30), len(ns[0])))

#RESOLUÇÃO DO PROFESSOR
n = str(input('Digite o nome completo: ')).strip()
print('........Total de letras:', len(n) - n.count(' '), '\nLetras do primeiro nome:', n.find(' '))