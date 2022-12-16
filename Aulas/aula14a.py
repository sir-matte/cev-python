# Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição while no Python. Por exemplo:
# c=1 while c !=10:
# print(c)
# c+=1
# print(‘Acabou’)

n = 1
p = i = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            p += 1
        else:
            i += 1
print('Voce digitou {} números pares e {} números ímpares.'.format(p, i))