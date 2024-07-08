#desafio 03: Cria um programa que vai gerar cinco números aleatórios a colocar em uma tupla.
    #Depois disso, mostra a listagem de números gerados e também indique o menor a o maior valor que estão na tupla.

from random import randint

num1 = int(randint(0,9))
num2 = int(randint(0,9))
num3 = int(randint(0,9))
num4 = int(randint(0,9))
num5 = int(randint(0,9))
numeros = (num1, num2, num3, num4, num5)
print(numeros)
print(f'O maior é {sorted(numeros)[4]} e o menor é {sorted(numeros)[0]}.')