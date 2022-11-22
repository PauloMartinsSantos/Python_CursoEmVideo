# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# para a condição ser verdadeira cada lado deve ser menor que a soma dos outros dois lados

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

if a < (b+c) and b < (a+c) and c < (a+b):
    print('>>>ESSES VALOREM FORMAM UM TRIÂNGULO<<<')
else:
    print('>>> ESSES VALORES NÃO FORMAM UM TRIÂNGULO<<<')
print('--FIM--')

