#desafio 01: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim a passo a realize a contagem. Seu programa tem que realizar três contagens através da função criada:
    #A) De 1 até 10, de 1 am 1
    #B) De 10 até 0, de 2 am 2
    #C) Uma contagem personalizada.

from time import sleep

def lin():
    print('=-='*15)

def contador(a, b, p):
    lin()
    print(f'Contagem de {a} a {b}, de {p} em {p}')
    sleep(2)
    
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    if a < b or p < 0:
        for n in range(a, b+1, p):
            print(f'{n} ', end='', flush=True)
            sleep(0.3)
        print('FIM!')
    else:
        for n in range(a, b-1, -p):
            print(f'{n} ', end='', flush=True)
            sleep(0.3)
        print('FIM!')
    

    
contador(1, 10, 1)
contador(10, 0, 2)
lin()
print('Agota é sua vez de fazer a contagem!')
a = int(input('Início: '))
b = int(input('Fim: '))
p = int(input('Passo: '))
contador(a, b, p)

