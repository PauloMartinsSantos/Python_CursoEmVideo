# Crie um algoritmo que leia um numero e mostre o seu dobro o seu triplo e a raiz quadrada.
n=int(input('Digite um número: '))
dobro=n*2
triplo=n*3
raiz=n**(1/2)

print('O dobro de {} é {}.\nO triplo é {}.\nA raiz quadrada é {:.2f}.'.format(n,dobro,triplo,raiz))