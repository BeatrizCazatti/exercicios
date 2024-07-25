#desafio 04: Mostre os 10 primeiros termos de uma PA a partir da leitura do primeiro termo e a razão desta.

a1 = int(input('Digite o primeiro termo:'))
r = int(input('Digite a razão:'))
an = a1 + r*(10)

for c in range(a1, an, r):
    print(c)
    