# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
from math import sin,cos,tan,radians
a = float(input('Digite um ângulo: '))

sen = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))

print('O ângulo de {}° tem o seno de {:.2f}'.format(a,sen))
print('O ângulo de {}° tem o cosseno de {:.2f}'.format(a,cos))
print('A ângulo de {}° tem a tangente de {:.2f}'.format(a,tan))
