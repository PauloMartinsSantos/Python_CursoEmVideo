# tempo=int(input('Quantos anos tem seu carro?'))
# if tempo <=3:
#     print('carro novo')
# else:
#     print('carro antigo')
# print('--FIM--')
#
# # ** Condição simplificada
#
# tempo=int(input('Quantos anos tem seu carro?'))
# print('carro novo')if tempo<=3 else'carro antigo')
# print('--FIM--')

# nome = str(input('Qual é o seu nome: '))
# if nome == 'Paulo':
#     print('Muito prazer em te conhecer!')
# print('Bom dia, {}'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2

print('A média do aluno foi {:.2f}'.format(m))
if m < 6:
    print('--RECUPERAÇÃO--')
else:
    print('--APROVADO--')
print('--Colégio Gafanhotos--')
