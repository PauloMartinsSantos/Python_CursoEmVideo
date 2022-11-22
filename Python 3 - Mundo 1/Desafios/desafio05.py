# Faça um programa que leia um numero inteiro e mostre o sucessor e o antecessor

n=int(input('Digite um número inteiro: '))
suc=n+1
ant=n-1

print('O sucessor de {} é {} e o antecessor é {}.'.format(n,suc,ant))
print('')

print('>>>>>>>>>> Versão com apenas uma variável <<<<<<<<<<')
n=int(input('Digite um número inteiro: '))
print('O sucessor de {} é {} e o antecessor é {}.'.format(n,(n+1),(n-1)))
