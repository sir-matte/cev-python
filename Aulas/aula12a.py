nome = str(input('Qual é seu nome? ')).title()
if nome == 'Gustavo':
    print('\033[1;4;31;42mQue nome bonito!\033[m')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('\033[32mSeu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('\033[1;34mBelo nome feminino!')
else:
    print('\033[1;33mSeu nome é bem normal.')
print('\033[1;4;36mTenha um bom dia, {}!\033[m'.format(nome))