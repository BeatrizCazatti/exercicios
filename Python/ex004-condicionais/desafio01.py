#desafio 01: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 a 5 a paça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
    #O programa deverá escrever na tela se o usuário venceu ou perdeu.

randonNumber = int()
inputNumber = int(input('Escolha um número de 1 a 5:'))

if randonNumber == inputNumber:
    print('Você acertou!')
else:
    print('Você errou!')