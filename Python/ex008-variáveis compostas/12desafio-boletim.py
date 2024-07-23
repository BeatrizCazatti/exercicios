#desafio 12: Crie um programa que leia nome e duas notas de vários alunos a guarde tudo em uma lista composta. No final, mostre um boletim contando a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

print('-'*25)
print(f'{"BOLETIM":^25}')
print('-'*25)

alunos = []

while True:
    nome = input('Nome:')
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    alunos.append([nome, nota1, nota2])
    if input('Quer continuar [S/N]? ').upper() != 'S':
        break

print('=-=-=-=-=   MÉDIA   =-=-=-=-=')
for pos, aluno in enumerate(alunos):
    print(f'{pos +1} {aluno[0]:.<20}', end='')
    media = (aluno[1] + aluno[2]) /2
    print(f'{media:>5}')

while True:
    print('=-='*15)
    index = int(input('Mostrar as notas do aluno com index: '))
    print('=-='*15)
    if index == 999:
        break
    print(f'Mostrando as notas de {alunos[index -1][0].upper():^5}')
    print(f'Nota 1: {alunos[index -1][1]}')
    print(f'Nota 2: {alunos[index -1][2]}')
