# Nessa aula, vamos aprender operações com String no Python.
# As principais operações que vamos aprender são
# Fatiamento de String, Análise com len(), count(), find(), transformações com replace()
# upper(), lower(), capitalize(), title(), strip(), junção com join().

frase = 'Harry Potter e a Pedra Filosofal'
print(frase[:12])
print(frase[13:])
print(frase[::2])
print(len(frase))
print('')
print(frase.count('t', 9, 32))
print(frase.find('Pedra'))
print('Potter' in frase)
print(frase.replace('Potter', 'Kane'))
print('')
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.split())
print('-'.join(frase))
print('-'.join(frase.split()))
print('')
frase = '     Camara Secreta       '
print(frase)
print(frase.strip())
print('''
Harry
Potter
e
o
Prisioneiro
de
Azkaban''')
