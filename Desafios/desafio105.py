# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um
# dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    r = {'total': len(n),
         'maior': max(n),
         'menor': min(n),
         'media': sum(n) / len(n)}
    if sit:
        if r['media'] < 6:
            r['situação'] = 'RAZOÁVEL'
        elif r['media'] > 7:
            r['situação'] = 'BOA'
        else:
            r['situação'] = 'RUIM'
    return r

#Programa principal
resp = notas(5.7, 8, 9.3)
print(resp)
