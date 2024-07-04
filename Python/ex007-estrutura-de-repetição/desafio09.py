#desafio 09: Crie um programa que leia dois valores e mostre um menu na tela e diga o respectivo resultado.
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa

num1 = int(input('Primeiro valor:'))
num2 = int(input('Segundo valor:'))

print('#'*20)
print('[1] somar \n[2] multiplicar \n[3] maior \n[4] novos números \n[5] sair do programa')
print('#'*20)
option = 0

while option != 5:
    option = int(input('Qual opção?'))
    match option:
        case 1:
            print('A soma é {}'.format(num1 + num2))
        case 2:
            print('A multiplação é {}'.format(num1 * num2))
        case 3:
            if num1 > num2:
                print('Entre {} e {}, o {} é maior.'.format(num1, num2, num1))
            else:
                print('Entre {} e {}, o {} é maior.'.format(num1, num2, num2))
        case 4:
            print('Digite dois valores novamente')
            num1 = int(input('Primeiro Valor:'))
            num2 = int(input('Segundo Valor:'))
    print('-==-'*5)