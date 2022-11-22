# Crie um programa que leia o nome de uma cidade e diga se ela começa com o nome 'SANTO'

# minha solução
c = str.upper(input('Digite o nome da cidade: '))
div = (c.split())
print(div[0] == 'SANTO')

# solução guanabara
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
