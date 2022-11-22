# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere US$ 1,00 = R$ 5,34

cart=float(input('Valor em R$: '))
usd=cart/5.34

print('Com o valor de R$ {:.2f} é possível comprar US$ {:.2f} dólares.'.format(cart,usd))