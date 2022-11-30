# Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# Equilátero: todos lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos lados diferentes

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

if a < (b+c) and b < (a+c) and c < (a+b):
    print('>>>ESSES VALORES FORMAM UM TRIÂNGULO<<<')
else:
    print('>>> ESSES VALORES NÃO FORMAM UM TRIÂNGULO<<<')


if a == b and b == c:
    print('==>> TRIÂNGULO EQUILÁTERO <<==')
elif a == b or a == c or b == c:
    print('==>> TRIÂNGULO ISÓSCELES <<==')
elif a != b and b != c:
    print('==>> TRIÂNGULO ESCALENO <<==')

print('--FIM--')
