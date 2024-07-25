#desafio 02: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep

def maior(* num):
    maior = count = 0
    sleep(0.5)
    print('=-='*10)
    print('Analisando os valores...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if maior == 0:
            maior = valor
        elif valor > maior:
            maior = valor
        count += 1
    print(f'Foram informados {count} valores ao todo.')
    print(f'O maior valor informado foi o {maior}.')

maior(2, 3, 9, 1, 4)
maior(3, 5, 3)
maior(9, 12)