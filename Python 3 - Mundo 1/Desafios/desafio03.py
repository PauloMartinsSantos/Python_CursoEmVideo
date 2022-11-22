# Crie um script python que leia dois números e mostre a soma entre eles

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
soma = num1 + num2
# print('A soma de', num1,'e', num2,'é:', soma )
print('A soma entre {} e {} é: {}'.format(num1, num2, soma))