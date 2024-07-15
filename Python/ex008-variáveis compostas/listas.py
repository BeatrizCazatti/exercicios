num = [2, 4, 9, 1]
num[3] = 8 # add 8 na posição 3
num.append(7) #adiciona um valor(7) ao final da lista
num.insert(2,5) #adiciona um valor(5) em determinada posição(2)
print(f'A lista {num} tem {len(num)} elementos.')
num.sort(reverse = True) #em ordem decrescente
num.pop() #retira o último elemento
num.pop(1) #retira o valor da posição 1
num.remove(2) #remove a primeira ocorrência do número 2 na lista
if 3 in num:
    num.remove(3)
else:
    print('Essa lista não tem o número 3')
#copiar listas:
a = [2, 3, 5, 8]
b = a[:] #copia a lista A de forma independente, sem fazer uma ligação entre elas
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')