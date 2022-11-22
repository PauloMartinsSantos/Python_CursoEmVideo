# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usúario tentar
# descobrir qual foi o número escolhido pelo computador.
from random import randint

# O programa deverá escrever se o usuário venceu ou perdeu

n = randint(0, 5)
print('')
print('----------TENTE ADIVINHAR QUAL NÚMERO FOI ESCOLHIDO PELO COMPUTADOR----------')
print('')
num = int(input('Escolha um número entre 0 e 5: '))

if n == num:
    print('PARABÉNS! VOCÊ ACERTOU')
else:
    print('NÃO FOI DESSA VEZ')
print('O número escolhido pelo PC foi {}'.format(n))
