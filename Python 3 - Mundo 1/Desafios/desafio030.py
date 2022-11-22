# Crie um programa que leia um número inteiro e mostre se ele é Par ou Impar

n = int(input('Digite um número inteiro: '))

if n % 2 == 0:
    print('O número {} é Par.'.format(n))
else:
    print('O número {} é Impar.'.format(n))
print('--FIM--')