# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude o professor,
# lendo o nome deles e escrevendo o nome do escolhido.
import random
al1 = input('Digite o nome do aluno 1: ')
al2 = input('Digite o nome do aluno 2: ')
al3 = input('Digite o nome do aluno 3: ')
al4 = input('Digite o nome do aluno 4: ')

lista = [al1, al2, al3, al4]

sorteado = random.choice(lista)


print('O aluno sorteado para apagar o quadro foi {}'.format(sorteado))

