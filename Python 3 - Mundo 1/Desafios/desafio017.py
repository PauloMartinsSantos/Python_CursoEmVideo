# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retangulo, calcule e
# mostre o comprimento da hipotenusa
# A soma dos quadrados dos catetos é igual a hipotenusa

from math import hypot

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

hypo = hypot(co,ca)

print('A medida da hipotenusa dos valores digitados é {:.2f}'.format(hypo))