# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

s = str(input('Informe seu sexo [M/F]: ')).strip()[0]
mf = ''
while s not in 'MmFf':
    print('')
    s = str(input('Dados inválidos.\nInforme seu sexo novamente [M/F]: ')).strip()[0]
if s in 'Mm':
    mf = 'masculino'
elif s in 'Ff':
    mf = 'feminino'
print('\nSexo {} registrado com sucesso.'.format(mf))
