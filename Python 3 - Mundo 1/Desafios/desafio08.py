# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
mt=float(input('Digite um valor em metros: '))
cm=mt*100
mm=mt*1000

print('{} metros equivale a {:.0f} cm e {:.0f} mm'.format(mt,cm,mm))