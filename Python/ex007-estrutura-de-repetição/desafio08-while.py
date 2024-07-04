#desafio 08: Melhora o jogo do DESAFIO01 das condicionais onde o computador vai "pensar" em um número entre 0 a 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

attempts = 1
randomNumber = int(randint(0,10))
inputNumber = int(input('Escolha um número de 0 a 10: '))

while inputNumber != randomNumber:  
    print('ERRADO')
    attempts += 1
    inputNumber = int(input('Tente outro:'))

if attempts == 0:
    print('ACERTOU de primeira!')
    
print('ACERTOU em {} tentativas'.format(attempts))