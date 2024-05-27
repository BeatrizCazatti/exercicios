#desafio 04:

a1 = int(input('Digite o primeiro termo:'))
r = int(input('Digite a razão:'))
an = a1 + r*(10)

for c in range(a1, an, r):
    print(c)
    