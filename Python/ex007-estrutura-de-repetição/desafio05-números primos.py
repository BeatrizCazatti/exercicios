#desafio 05: Faça um programa que leia um  número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número:'))
total = 0

for c in range(1, num+1):
    if num % c == 0:
        print('\033[0;32m {} \033[m'.format(c), end='')
        total += 1
    else:
        print('\033[0;31m {} \033[m'.format(c), end='')

print('\nO número {} foi divisível {} vezes'.format(num, total))

if total == 2:
    print('E por isso ele é PRIMO')
else:        
    print('E por isso ele NÃO é PRIMO')
