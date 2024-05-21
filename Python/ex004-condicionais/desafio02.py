#desafio 05: Faça um programa que leia três números e mostra qual é o maior e qual é o menor.

n1 = int(input('primeiro número:'))
n2 = int(input('segundo número:'))
n3 = int(input('terceiro número:'))

if n1 > n2:
    if n1 > n3:
        if n3 > n2:
            #n2 n3 n1
            print(f'{n1} é o maior')
            print(f'{n2} é o menor')
        else:
            #n3 n2 n1
            print(f'{n1} é o maior')
            print(f'{n3} é o menor')
    else:
        #n2 n1 n3
        print(f'{n3} é o maior')
        print(f'{n2} é o menor')
else:
    if n1 > n3:
        #n3 n1 n2
        print(f'{n2} é o maior')
        print(f'{n3} é o menor')
    else:
        if n3 > n2:
            #n1 n2 n3
            print(f'{n3} é o maior')
            print(f'{n1} é o menor')
        else:
            #n1 n3 n2
            print(f'{n2} é o maior')
            print(f'{n1} é o menor')