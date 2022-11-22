# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
n=int(input('Digite um número inteiro: '))
print('\nA tabuada de {} é:\n '.format(n))

for i in range(10):
    print('{} x {} = {}'.format(n,i+1,n*(i+1)))
print('')    