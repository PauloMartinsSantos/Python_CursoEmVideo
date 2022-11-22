# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada
# litro de tinta pinta uma área de 2M²

l=float(input('Digite a largura em M²: '))
h=float(input('Digite a altura em M²: '))
area=l*h
tinta= area/2

print('Área total: {:.2f}'.format(area))
print('É necessário {:.2f} lts de tinta para cobrir a área total.'.format(tinta))