# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
nome = str(input('Digite seu nome completo: ')).strip()

print('Nome: ' + nome)
n = nome.split()
print('first name: {}'.format(n[0]))
print('last name:  {}'.format(n[len(n)-1]))
