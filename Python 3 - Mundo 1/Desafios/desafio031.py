# Escreva um programa que pergunte a distância de uma viagem em KM.
# Calcule o preço da passagem cobrando R$0,50 por KM para viagens de até 200Km e R$0,45 para viagens mais longas.

dist = float(input('Digite a distância da viagem em KM: '))

if dist <= 200:
    print('O valor da passagem é R$ {}'.format(dist * 0.50))
else:
    print('O valor da passagem é R$ {}'.format(dist * 0.45))
