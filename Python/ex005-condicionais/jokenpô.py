from random import randint
print('#'*10)
print('1-Pedra \n2-Papel \n3-Tesoura')
print('#'*10)

escolhaPC = int(randint(1,3))
escolhaPlayer = int(input('Escolha:'))

if escolhaPlayer == 1:
    print('Você: PEDRA')
elif escolhaPlayer == 2:
    print('Você: PAPEL')
elif escolhaPlayer == 3:
    print('Você: TESOURA')

if escolhaPC == 1:
    print('Computador: PEDRA')
elif escolhaPC == 2:
    print('Computador: PAPEL')
elif escolhaPC == 3:
    print('Computador: TESOURA')

if escolhaPlayer == escolhaPC:
    print('EMPATE')
elif escolhaPlayer == 1 and escolhaPC == 3 or escolhaPlayer == 2 and escolhaPC == 1 or escolhaPlayer == 3 and escolhaPC == 2:
    print('VENCEU')
else:
    print('PERDEU')