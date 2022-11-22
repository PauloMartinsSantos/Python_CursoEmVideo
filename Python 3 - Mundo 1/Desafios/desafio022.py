# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras no total (sem considerar os espaços)
# Quantas letras tem o primeiro nome

# Minha solução
nome = str(input('Digite seu nome completo: '))

print(nome.upper())
print(nome.lower())
nome.replace(" ", "")
print(nome.replace(" ", ""))
print(len("".join(nome.split())))
div = nome.split()
print(len(div[0]))

# Solução Guanabara
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {}'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))


