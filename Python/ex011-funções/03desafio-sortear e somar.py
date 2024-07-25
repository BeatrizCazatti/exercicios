#desafio 03: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números a vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
from random import randint

numeros = []
def sorteia():
    for c in range(0, 5):
        num = randint(0,10)
        numeros.append(num)
    print(f'A lista sorteada foi: {numeros}.')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma de todos os valores pares é {soma}.')


sorteia()
somaPar(numeros)