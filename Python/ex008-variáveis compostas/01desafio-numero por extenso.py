#desafio 01: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
    #Seu programa deverá ler um número pelo teclado (entre 0 a 20) a mostrá-lo por extenso.

numerosExtenso = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
num = int(input('Digite um número de 0 a 20:'))

for c in range(0, 20):
    if num == c:
        print(f'{numerosExtenso[c]}')
        break
