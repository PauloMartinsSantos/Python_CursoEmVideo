## Operadores Aritiméticos ##

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
soma = num1 + num2
mult = num1 * num2
div  = num1 / num2
di   = num1 // num2
exp  = num1 ** num2
print ('A soma é {}, o produto é {} a divisão é {:.2f}'.format(soma, mult, div),end =' ')
print ('a divisão inteira é {} e a exponenciação é {}.'.format(di, exp))

