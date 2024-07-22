#desafio 09: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares a ímpares. No final mostre os valores pares e ímpares em ordem crescente.

pares = []
impares = []
num = 0

for n in range(1, 8):
    num = int(input(f'Digite o {n}º valor:'))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    
pares.sort()
impares.sort()
lista = [pares[:], impares[:]]
print(f'Os valores pares digitados foram {lista[0]}.')
print(f'Os valores ímpares digitados foram {lista[1]}.')