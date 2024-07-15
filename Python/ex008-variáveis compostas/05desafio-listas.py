#desafio 05: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
    #No final, mostre qual foi o maior a o menor valor digitado a as suas respectivas posições na lista.

lista = []

for n in range(0, 5):
    lista.append(int(input('Número:')))
print(lista)

listaOrdenada = lista[:]
listaOrdenada.sort()
menor = listaOrdenada[0]
maior = listaOrdenada[len(lista) - 1]

print(f'O menor é {menor} que está na posição {lista.index(menor)}')
print(f'O maior é {maior} que está na posição {lista.index(maior)}')