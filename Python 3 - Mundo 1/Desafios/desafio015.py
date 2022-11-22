#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

qtdDias = int(input('Digite a quantidade de dias do aluguel do carro: '))
km=float(input('Digite a quantidade de KM rodado: '))

res=(qtdDias*60)+(km*0.15)

print('O valor total do aluguel é R$ {:.2f}'.format(res))