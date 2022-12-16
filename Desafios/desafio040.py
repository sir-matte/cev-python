# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

print('''MÉDIA DAS NOTAS
-----------''')
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
s = (n1 + n2) / 2
if s < 5:
    print('Média = \033[31m{:.1f}\n\033[4;1mREPROVADO'.format(s))
elif 5 < s < 7:
    print('Média = \033[33m{:.1f}\n\033[4;1mRECUPERAÇÃO'.format(s))
else:
    print('Média = \033[32m{:.1f}\n\033[4;1mAPROVADO'.format(s))
