#desafio 08: Faça um programa que leia nome a peso de várias pessoas. Guardando tudo em uma lista. No final mostre:
    #A) Quantas pessoas foram cadastradas.
    #B) Uma listagem com as pessoas mais pesadas.
    #C) Uma listagam com as pessoas mais leves.

maisPesado = 0
maisLeve = 0
lista = []

while True:
    nome = str(input('Nome:'))
    peso = float(input('Peso:'))

    if peso > maisPesado:
        maisPesado = peso
    if peso < maisLeve or maisLeve == 0:
        maisLeve = peso

    lista.append([nome,peso])

    if input('Quer continuar [S/N]?').upper() != 'S':
        print('=-='*20)
        pesados = []
        leves = []
        for p in lista:
            if p[1] == maisPesado:
                pesados.append(p[0])
            if p[1] == maisLeve:
                leves.append(p[0])

        print(f'Foram cadastradas {len(lista)} pessoas.')
        print(f'O maior peso foi {maisPesado}Kg. Peso de {pesados}')
        print(f'O maior peso foi {maisPesado}Kg. Peso de {leves}')
        break