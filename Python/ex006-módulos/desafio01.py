#Sorteie uma ordem de apresentação a partir da leitura de quatro nomes
from random import shuffle

n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))

lista = [n1,n2,n3,n4]
print('nomes inseridos: {}'.format(lista))
shuffle(lista)
print('ordem sorteada: {}'.format(lista))
