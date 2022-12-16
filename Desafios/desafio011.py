# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS
# CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA
# SABENDO QUE CADA LITRO DE TINTA PINTA UMA AREA DE 2M².
print('Vamos pintar sua parede!\n')
l = float(input('Largura da parede em metros: '))
a = float(input('Altura da parede em metros: '))
area = l * a
t = area / 2

print('Área da parede =', area,'metros\nLitros de tinta necessários para pintar toda a parede =', t, 'litros')
