# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a
# média atingida
# Média abaixo de 5.0: Reprovado
# Média entre 5.0 e 6.9: Recuperação
# Média 7.0 ou superior: Aprovado

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
med = (n1+n2)/2
if med < 5:
    print('A média do aluno foi {:.2f}'.format(med))
    print('==>> ALUNO REPROVADO <<==')
elif med > 5 and med <= 6.9:
    print('A média do aluno foi {:.2f}'.format(med))
    print('==>> ALUNO DE RECUPERAÇÃO <<==')
else:
    print('A média do aluno foi {:.2f}'.format(med))
    print('==>> ALUNO APROVADO <<==')

