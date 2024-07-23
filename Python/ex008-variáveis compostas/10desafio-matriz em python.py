#desafio 10: Crie um programa que cria uma matriz da dimensão 3x3 e preencha com valores lidos pelo teclado.
    #No final, mostre a matriz na tela com a formatação correta.

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
somaTerceiraColuna = 0
maiorSegundaLinha = 0
somaPares = 0

print('=-='*10)
print(f'{"MATRIZ":^30}')
print('=-='*10)
for lin in range(0, 3):
    for col in range(0 , 3):
        matriz[lin][col] = int(input(f'Digite um valor para [ {lin}, {col} ]: '))
        if matriz[lin][col] % 2 == 0:
            somaPares += matriz[lin][col]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if c == 3 -1:
            somaTerceiraColuna += matriz[l][2]
        if l == 2 -1:
            if matriz[1][c] > maiorSegundaLinha or maiorSegundaLinha == 0:
                maiorSegundaLinha = matriz[1][c]
    print('\n')

#Aprimore o desafio anterior, mostrando no final:
    #A) A soma de todos os valores pares digitados.
    #B) A soma dos valores da terceira coluna.
    #C) O maior valor da segunda linha.

print(f'A soma de todos os valores pares digitados é {somaPares}')
print(f'A soma dos valores da terceira coluna é {somaTerceiraColuna}')
print(f'O maior valor da segunda linha é {maiorSegundaLinha}')