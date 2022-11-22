# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c=float(input('Digite a temperatura em °C: '))
f= c*1.8+32

print('A temperatura de {:.1f} °Celsius equivale a {:.1f} °Farenheit'.format(c,f))