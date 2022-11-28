# Escreva um programa para aprovar um empréstimo bancário para compra de uma casa. O programa vai perguntar o valor
# do financiamento, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será
# negado max 30 anos (360 meses).

print('>>>>>SIMULADOR DE FINANCIAMENTO<<<<<\n')
valor = float(input('Digite o valor do financiamento R$: '))
qtdAnos = float(input('Digite em quantidade de anos do financiamento (limite 30 anos): '))
sal = float(input('Digite a renda mensal R$: '))
parc = valor / (qtdAnos*12)

if sal*0.3 < parc:
    print('O valor das parcelas é R$ {:.2f} mensais'.format(parc))
    print('A renda atual não comporta o valor da parcela pois ultrapassa 30% da renda mensal')
    print('Valor máximo por parcela : R$ {:.2f}'.format(sal*0.3))
if qtdAnos < 30:
    print('>>>Tente efetuar uma nova simulação aumentando o tempo de financiamento<<<')

else:
    print('\n>>>FINANCIAMENTO PRÉ APROVADO<<<\n')
    print('Valor das parcelas: R$ {:.2f}'.format(parc))
    print('Quantidade de parcelas: {:.0f}'.format(qtdAnos*12))
    print('Valor total financiado: R$ {}'.format(valor))







