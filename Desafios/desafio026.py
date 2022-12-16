# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

f = str(input('Digite uma frase:\n')).upper().strip()
print('Letra "A" aparece {} vezes\nPrimeira vez na posição {}\nÚltima vez na posição {}'
      .format(f.count('A'), f.find('A')+1, f.rfind('A')+1))
