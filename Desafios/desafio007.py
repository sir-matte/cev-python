# DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO, CALCULE E MOSTRE A SUA MÉDIA

n1 = float(input('\033[4;1;35mPrimeira nota: '))
n2 = float(input('\033[4;1;34mSegunda nota: '))
print('\033[1;4;30;46mA média das notas é {:.1f}\033[m'.format((n1+n2)/2))
