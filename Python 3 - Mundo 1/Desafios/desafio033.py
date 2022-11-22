# Faça um programa que leia três números e mostre qual é o maior e qual o menor

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor:  '))
n3 = float(input('Digite o terceiro valor: '))

maior = ''
menor = ''

# menor
if n1 < n2:
    if n1 < n3:
        menor = n1
    else:
        menor = n3
else:
    if n2 < n3:
        menor = n2
    else:
        menor = n3

# maior
if n1 > n2:
    if n1 > n3:
        maior = n1
    else:
        maior = n3
else:
    if n2 > n3:
        maior = n2
    else:
        maior = n3

print ('Números digitados {}, {}, e {}'.format(n1,n2,n3))
print('O maior número digitado foi {}'.format(maior))
print('O menor número digitado foi {}'.format(menor))



