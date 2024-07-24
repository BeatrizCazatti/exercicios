#desafio 11: Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados a vai sortear 6 números entre 1 e 60 para cada jogo. Cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

print('-'*30)
print(f'{"JOGOS NA MEGA SENA":^30}')
print('-'*30)
numJogos = int(input('Quantos jogos você quer que eu sorteie? '))
todosJogos = []


print(f'=-=-=-=-= SORTEANDO {numJogos} JOGOS =-=-=-=-=')

for n in range(1, numJogos + 1):
    jogo = []
    sleep(1)
    for num in range(0, 7):
        num = randint(0, 60)
        jogo.append(num)
    todosJogos.append(jogo[:])
    print(f'Jogo {n}: {jogo}')

print(f'=-=-=-=-=-=-= BOA SORTE =-=-=-=-=-=-=')
    