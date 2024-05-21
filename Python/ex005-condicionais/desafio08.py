#desafio 08: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#- 1 para binário
#- 2 para octal
#- 3 para hexadecimal
num = int(input('Digite um número inteiro:'))

print('#'*20)
print('1-para binário \n2-para octal \n3-para hexadecimal')
print('#'*20)

base = int(input('Escolha a opção de conversão:'))

if base == 1:
    print('O número em base binária é {}')
elif base == 2:
    print('O número em base octal é {}')
elif base == 3:
    print('O número em base hexadecimal é {}')



