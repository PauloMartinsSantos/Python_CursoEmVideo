import math
import random
import emoji

print('\n>>>>>>>>>> CÁLCULO RAIZ QUADRADA <<<<<<<<<<\n')
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é {:.2f}'.format(num, raiz))
print('')

print('>>>>>>>>>> RAIZ QUADRADA DE UM NÚMERO ALEATÓRIO <<<<<<<<<<')
num = random.randint(1, 999)
raiz = math.sqrt(num)
start = input(
    'Este código escolhe um número aleatório entre 1 e 999 e calcula sua raiz quadrada, pressione uma Enter para'
    ' continuar...')
print('A raiz quadrada de {} é {:.2f}'.format(num, raiz))
print('')

print('>>>>>>>>>> BIBLIOTECA EMOJI <<<<<<<<<<')
print(emoji.emojize('Olá mundo! :earth_americas:', language='alias'))
print(emoji.emojize("Python is fun :red_heart:", variant="text_type"))
print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
