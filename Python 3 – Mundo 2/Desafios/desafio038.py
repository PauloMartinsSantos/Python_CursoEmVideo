# Escreva um programa que leia dois números inteiros e compare-is, mostrando na tela uma mensagem:

# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('==>> Valores digitados {} e {} <<=='.format(n1, n2))

if n1 > n2:
    print('\n- O primeiro valor é o maior.')
elif n2 > n1:
    print('\n- O segundo valor é o maior.')
else:
    print('\n- Não existe valor maior, os dois são iguais.')
