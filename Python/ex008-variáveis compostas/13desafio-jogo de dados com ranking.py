#desafio 13: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, mostre um ranking dos jogadores. 

from random import randint
from time import sleep
from operator import itemgetter
jogos = {}

for n in range(1, 5):
    num = randint(1,6)
    print(f'O jogador{n} sorteou {num}')
    jogos[f'jogador{n}'] = num
    sleep(1)

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)

print('=-='*15)
print(f'{"RANKING":^45}')
print('=-='*15)
sleep(2)

for n in range(1, 5):
    print(f'    => {n}º lugar {ranking[n-1][0]} tirou {ranking[n-1][1]}')
    sleep(1.3)
print('=-='*15)