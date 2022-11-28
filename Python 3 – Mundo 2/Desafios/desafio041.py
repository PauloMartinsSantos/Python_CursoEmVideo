# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria de acordo com a idade:
# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 20 anos: Sênior
# Acima: Master
import datetime
date = datetime.date.today()
nasc = int(input('Digite o ano de nascimento com 4 dígitos: '))
idade = date.year - nasc

if idade <= 9:
    print('==>> CATEGORIA MIRIM <<==')
elif idade <= 14:
    print('==>> CATEGORIA INFANTIL <<==')
elif idade <= 19:
    print('==>> CATEGORIA JUNIOR <<==')
elif idade  == 20:
    print('==>> CATEGORIA SÊNIOR <<==')
else:
    print('==>> CATEGORIA MASTER <<==')



