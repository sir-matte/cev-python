# Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
# As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
# acessíveis por chaves individuais.

teste = []
teste.append('Gustavo')
teste.append(25)
galera = []
galera.append(teste[:])
teste[0] = 'Desi'
teste[1] = 24
galera.append(teste[:])
print(galera, '\n--------------------------------')

galera = [['João', 19], ['Pedro', 21], ['Carla', 26], ['Tomas', 17]]
print(galera[2][0])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
print('-------------------------------------')

galera = []
dado = []
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores de idade, e {totmen} menores de idade')