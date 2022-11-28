# Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:

# - Se ainda vai se alistar
# - Se é hora de se alistar
# - Se ja passou do tempo do alistamento
# Mostrar também quanto tempo falta para se alistar ou quanto tempo ja passou
import datetime
nasc = int(input('Digite o ano de nascimento com 4 dígitos: '))
date = datetime.date.today()
idade = date.year - nasc


if idade < 18:
    print('Você ainda deve se alistar')
    print('Faltam {} anos para o alistamento'.format(18 - idade))
elif idade == 18:
    print('Você esta no ano de alistamento.')
elif idade > 18:
    print('Você passou do tempo de alistamento')
    print('O prazo de alistamento esta atrasado em {} anos'.format(idade - 18))