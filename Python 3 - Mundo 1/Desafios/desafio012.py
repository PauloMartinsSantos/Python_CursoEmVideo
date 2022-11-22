# Faça um algoritimo que leia o preço de um produto e mostre o novo preço com 5% de desconto
produto=float(input('Valor do produto R$: '))
print('Valor com desconto R$ {:.2f}'.format(produto-(produto*0.05)))