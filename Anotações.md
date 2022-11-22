
## Operadores aritiméticos ##

+ : Adição
- : Subtração
* : Multiplicação
/ : Divisão
** : Potêcia
// : Divisão inteira
% : Resto da divisão (módulo)

## Ordem de precedência ##

1 = ()
2 = **
3 = * / // %
4 = + - 

5+2 == 7
5-2 == 3
5*2 == 10
5/2 == 2.5
5**2 == 25
5//2 == 2
5%2 == 1

## Módulos ##
math
    ceil
    floor
    trunc
    pow
    sqrt
    factorial


Importando o módulo completo
    import > math

Importando apenas uma funcionalidade 
    from > math > import > sqrt

Importando algumas funcionalidades
    from > math > import > sqrt,pow

## Bibliotecas externas ##

acessar python.org > pypi
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Manipulação de texto ## (Aula 09)
    frase = 'Curso em Vídeo Python'
  ____________________________________________________________________________________
# | C | u | r | s | o |   | e | m |   | V | í | d | e | o |   | P | y | t | h | o | n |
    0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  

    Fatiamento
     frase[9] V
     frase[9:13] Víde
     frase[9:21] Vídeo Python
     frase[9:21:2] VdoPto (Inicia no 9 vai até o 20 pulando de 2 em 2)
     frase[:5] Curso      (Quando omitido o inicio o fatiamento começa da posição 0)
     frase[15:] Python    (Ao não indicar o fim o fatiamento vai até o final do texto)
     frase[9::3] VePh     (Inicia do 9 vai até o fim do texto e pula de 3 em 3)

    Análise
     len(frase) ** Comprimento da frase
     frase.count('o',0,13) ** conta a quantidade de letra 'o' na frase após a vírgula definimos inicio e fim da varredura
     frase.find('deo') retorna quantas vezes a palavra foi encontrada
     frase.find('Android')  ao buscar uma palavra que não existe o python retorna -1 se existir retorna 0
     'Curso' in frase ** Existe a palavra '' na frase? retorno True

    Transformação
     frase.replace('Python', 'Android') ** Busca e substitui 
     frase.upper()  **Todas letras maiúsculas
     frase.lower*() ** Todas letras minúsculas
     frase.captalize() **Somente o primeiro caracter em maiúsculo
     frase.title() **Primeira letra de cada palavra maiúscula

     frase =  '   Aprenda Python  '
     ___________________________________________________________________________
# |   |   |   | A | p | r  | e | n | d  | a |  | P | y | t | h  | o | n |  |   |
    0   1   2   3   4   5    6   7   8    9  10  11  12  13  14  15  16  17  18  

     frase.strip() **Remove os espaços desnecessários (antes e depois)
     frase.rstrip() **Remove os espaços do fim da frase (os espaços a direita), nesse exemplo as posições 17 e 18
     frase.lstrip() **Remove os espaços do inicio da frase (os espaços a esquerda), nesse exemplo as posições 0, 1 e 2
     
     frase.split()  **Cada palavra recebe uma nova indexação
   ____________________   _________   _____________________   _________________________
# | C | u | r | s | o |   | e | m |   | V | í | d | e | o |   | P | y | t | h | o | n |
    0   1   2   3   4       0   1       0   1   2   3   4       0   1   2   3   4   5
            0                 1                 2                          3

    para realizar o processo inverso:
    '-'.join(frase)
    perceba que foi adicionado um traço '-' nos espaços para alterar basta colocar o caracter desejado antes do .join
    ____________________________________________________________________________________
# | C | u | r | s | o | - | e | m | - | V | í | d | e | o | - | P | y | t | h | o | n |
    0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20 
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
               
### Condições ### Aula 10
    Exemplo de repetição
carro.siga()    
se carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
senão
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
carro.pare()       

Neste exemplo o comando inicial 'carro.siga()' e o comando final 'carro.pare()' serão executados independente da escolha de direção, isso por conta da identação. 

se carro.esquerda() 
    bloco_V_
senão
    bloco_F_

if carro.esquerda():
    bloco True
else:
    bloco False

Exemplo 2:

tempo=int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print('carro novo')
else:
    print('carro antigo')
print('--FIM--')

** Condição simplificada
tempo=int(input('Quantos anos tem seu carro?'))
print('carro novo')if tempo<=3 else'carro antigo')
print('--FIM--')


