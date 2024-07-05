#desafio 13: Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER. Mostrando o total de vitórias consecutivas que ela conquistou no final do jogo.

from random import randint

print('=-='*10)
print('JOGAR PAR OU ÍMPAR')
print('=-='*10)


while True:
    valorPC = int(randint(0,100))
    valorUser = int(input('Digite um valor:'))
    escolhaUser = str(input('Escolha [P/I]:')).upper()
    soma = int(0)

    print(f'O computador escolheu {valorPC}')
    soma = valorPC + valorUser
    print(f'{valorUser} com {valorPC} dá {soma}, um número ', end='')
    if soma % 2 == 0:
        print('PAR')

        if escolhaUser == 'P':
            print('ACERTOU')
        else:
            print('PERDEU')
            break
    else:
        print('ÍMPAR')

        if escolhaUser == 'I':
            print('ACERTOU')
        else:
            print('PERDEU')
            break
    print('='*20)
    print('Jogando novamente...')
    print('='*20)

    
        
    
