#desafio 14: Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunta ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
    #OBS: Considerando que o caixa possui cédulas de R$50, R$20, R$10 a R$1.

print('='*25)
print('BANCO DA BEA')
print('='*25)
valor = int(input('Digite o valor que quer sacar:'))

while valor > 0:
    if valor // 50 != 0:
        print(f'{valor // 50} nota de 50')
        valor -= (valor // 50)*50
        if valor == 0:
            break
    if valor // 20 != 0:
        print(f'{valor // 20} nota de 20')
        valor -= (valor // 20)*20
        if valor == 0:
            break
    if valor // 10 != 0:
        print(f'{valor // 10} nota de 10')
        valor -= (valor // 10)*10
        if valor == 0:
            break
    if valor // 1 != 0:
        print(f'{valor // 1} nota de 1')
        valor -= valor // 1
        if valor == 0:
            break
