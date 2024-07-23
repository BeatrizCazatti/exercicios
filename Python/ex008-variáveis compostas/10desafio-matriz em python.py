#desafio 10: Crie um programa que cria uma matriz da dimensão 3x3 e preencha com valores lidos pelo teclado.
    #No final, mostre a matriz na tela com a formatação correta.

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print('=-='*10)
print(f'{"MATRIZ":^30}')
print('=-='*10)
for lin in range(0, 3):
    for col in range(0 , 3):
        matriz[lin][col] = int(input(f'Digite um valor para [ {lin}, {col} ]: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print('\n')
