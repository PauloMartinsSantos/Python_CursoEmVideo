# Crie um programa que leia um número Real qualquer e mostre na tela a sua porção inteira
# Ex : 6.127 > 6.
from math import trunc
n = float(input('Digite um número Real: '))

print('A parte inteira de {} é {:.0f}'.format(n,n))
print('A parte inteira de {} é {}'.format(n,trunc(n)))
print('A parte inteira de {} é {}'.format(n,int(n)))



