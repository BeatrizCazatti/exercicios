#desafio 04: Crie um programa que tenha uma tupla única com nomes de produtos a seus respectivos preços, na sequência.
    #No final, mostra uma listagem de preços, organizando os dados em forma tabular.

lista = ('Lápis', 1.85, 
        'Borracha', 2,
        'Caderno', 5.50, 
        'Régua', 3.20, 
        'Caneta', 1.50 
        'Mochila', 80.00, 
        'Estojo', 10.50)

for pos in lista:
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}')