# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada KM acima do limite.

v = float(input('Digite a velocidade em Km/h: '))
m = ''

print('----------- VELOCIDADE MAX PERMITIDA 80KM -----------')
if v > 80:
    m = (v - 80) * 7
    print('---------------------MULTADO-------------------------')
    print('O valor da multa esta calculado em R$ {:.2f}'.format(m))
