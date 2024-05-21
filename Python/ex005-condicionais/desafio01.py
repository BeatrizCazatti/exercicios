#desafio 01: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 a 5 a paça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
    #O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

randomNumber = int(randint(1,5))
inputNumber = int(input('Escolha um número de 1 a 5: '))

if inputNumber == randomNumber:
    print('ACERTOU')
else:
    print('ERROU era o número {}.'.format(randomNumber))