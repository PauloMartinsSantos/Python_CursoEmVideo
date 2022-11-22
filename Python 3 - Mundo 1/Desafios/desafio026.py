# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A'
# Em que posição ela aparece a primera vez
# Em que posição ela aparece a última vez

frase = str.upper(input('Digite uma frase: ')).strip()
print('Esta frase contém {} letra(s) A'.format(frase.count('A')))
print('A primeira ocorrência esta na posição {}'.format(frase.find('A')+1))
print('A última ocorrência esta na posição {}'.format(frase.rfind('A')+1))

