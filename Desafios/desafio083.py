# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

print('\033[1;36mEXPRESSÕES COM PARÊNTESES\033[m')
e = str(input('Digite a expressão: ')) #expressão
p = [] #pilha
for s in e: #para 'símbolos' em 'expressão'
    if s == '(':
        p.append('(') #acrescenta em 'pilha'
    elif s == ')':
        if len(p) > 0: #tamanho de 'pilha'
            p.pop() #excluir último item da 'pilha'
        else:
            p.append(')')
if len(p) > 0:
    print('Sua expressão está inválida!')
else:
    print('Sua expressão é válida!')



