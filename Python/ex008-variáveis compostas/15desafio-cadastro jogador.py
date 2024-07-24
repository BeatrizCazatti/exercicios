#desafio 15: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}

nome = str(input('Nome: '))
jogador['nome'] = nome

partidas = int(input(f' Quantas partidas {nome} jogou? '))
gols = []
total = 0

for n in range(1, partidas +1):
    num = int(input(f'Gols feitos no {n}ºjogo: '))
    gols.append(num)
    total += num
jogador['gols'] = gols
jogador['total'] = total

print('=-='*20)
print(jogador)
print('=-='*20)