# Vamos criar um 1menu em Python, usando modularização.
# Vamos ver como fazer acesso a arquivos usando o Python.
# Vamos finalizar o projeto de acesso a arquivos em Python.

from lib.arquivo import *
from lib.interface import *

arq = 'cadastro.txt'
if not arqExiste(arq):
    criarArq('cadastro.txt')
while True:
    o = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Excluir conteúdo', 'Sair do sistema'])
    if o == 1:
        lerArq(arq)
    elif o == 2:
        cabeçalho('CADASTRAR NOVA PESSOA')
        nome = (str(input('Nome: ')).strip().title())
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif o == 3:
        limpar(arq)
        cabeçalho('CONTEÚDO EXCLUÍDO')
    elif o == 4:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print(cores('ERRO: digite uma opção válida.', 1))

