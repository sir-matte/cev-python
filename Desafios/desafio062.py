# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('''\033[1;36m============================
    DEZ TERMOS DE UMA PA
============================\033[0;35m''')
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
ct = 0
while c < 10:
    ct += 1
    c += 1
    print(t, end=' → ')
    t += r
    if c == 10:
        print('\033[31mPAUSA\033[34m')
        st = int(input('Quantos termos você quer mostrar a mais? \033[35m'))
        if st > 0:
            c -= st
        else:
            print('\033[31mACABOU\033[34m')
print('Finalizado mostrando {} termos no total'.format(ct))
