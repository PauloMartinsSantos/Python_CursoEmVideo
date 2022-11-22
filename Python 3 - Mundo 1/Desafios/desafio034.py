# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

# Para Salários superiores a R$1250 o aumento é de 10%
# Para salários inferiores ou iguais a R$1250 o aumento é de 15%

sa = float(input('Digite o sálario atual R$: '))
ns = ''
if sa > 1250:
    ns = sa + sa * 0.10
    print('O novo salário é R$ {:.2f}'.format(ns))
else:
    ns = sa + sa * 0.15
    print('O novo salário é R$ {:.2f}'.format(ns))
print('--FIM--')