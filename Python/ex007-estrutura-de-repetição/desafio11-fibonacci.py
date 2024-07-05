#desafio 11: Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.

#Sequência de Fibonacci: é um padrão numérico em que o primeiro e o segundo termo são iguais a 1 e cada termo a partir do terceiro é a soma dos dois termos anteriores.


print('-'*20)
print('Sequência de Fibonacci')
print('-'*20)

n = int(input('Quantos números você quer mostrar?'))
#0 -> 1 -> 1 -> 2 -> 3 -> 5
print('~'*20)
print('0 -> 1 ->', end='')

n1 = 0
n2 = 1
c = 2
while c < n:
    n3 = n1 + n2
    c += 1
    print(' {} '.format(n3), end='')
    print('->' if c != n else '= FIM', end='')
    n1 = n2
    n2 = n3