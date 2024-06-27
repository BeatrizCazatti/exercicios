#desafio 06: Cria um programa que leia uma frase qualquer e diga se ela é um palindromo. Desconsiderando os espaços.

frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

print('O inverso da palavra {} é {}'.format(junto, inverso))

if junto == inverso:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')

