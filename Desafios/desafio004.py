algo = str((input('\033[1;4mDigite algo:\033[m ')))
print('\033[31mTipo primitivo:\033[m', type(algo))
print('\033[32mÉ um número? ', algo.isnumeric())
print('\033[33mÉ alfabético? ', algo.isalpha())
print('\033[34mEstá em maiúsculas? ', algo.isupper())
print('\033[35mEstá em minúsculas? ', algo.islower())
print('\033[36mEstá capitalizada? ', algo.istitle())
print('\033[30mÉ alfanumérico? ', algo.isalnum())