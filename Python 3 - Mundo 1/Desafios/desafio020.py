# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
al1 = input('Digite o nome do aluno 1: ')
al2 = input('Digite o nome do aluno 2: ')
al3 = input('Digite o nome do aluno 3: ')
al4 = input('Digite o nome do aluno 4: ')
lista = [al1, al2, al3, al4]
shuffle(lista)

print('A ordem de apresentação será: ')
print(lista)
