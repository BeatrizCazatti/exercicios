#desafio 06: Cria um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro. Ela não será adicionado. 
    #No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []

while True:
    num = int(input('Digite um número:'))
    if num in lista:
        print('Número duplicado! Valor não cadastrado.')
    else:
        lista.append(num)
    if input('Quer continuar [S/N]?').upper() != 'S':
        lista.sort()
        print(lista)
        break
