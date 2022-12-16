# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

#MINHA RESOLUÇÃO
n = str(input('Digite o nome completo: ')).split()
print('Primeiro nome: ', n[0])
n.reverse()
print('Último nome: ', n[0])
print('')

#RESOLUÇÃO DO PROFESSOR
nome = str(input('Digite o nome completo: ')).split()
print('Primeiro nome: {} \nÚltimo nome: {}'.format(nome[0], nome[len(nome)-1]))
