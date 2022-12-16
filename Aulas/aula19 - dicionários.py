pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 25}
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()

estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).title()
    estado['sigla'] = str(input('Sigla do Estado: ')).upper()
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()