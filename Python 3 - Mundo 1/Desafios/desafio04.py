# Faça um programa que leia algo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('Digite algo: ')

print('Informações do dado digitado: [True] é verdadeiro e [False] é falso')
print('')
print('O tipo primitivo do dado é: ', type(n))
print('Dado é numérico:       ',n.isnumeric())
print('Dado é alfanumérico:   ',n.isalnum())
print('Dado é todo minusculo: ',n.islower())
print('Dado é todo maiúsculo: ',n.isupper())
