def lin(txt):
    tam = len(txt) + 4
    print('-'*tam)
    print(f'  {txt.upper():^}  ')
    print('-'*tam)
def soma(a, b):
    print(a + b)
def contador(* num):
    print(f'Recebi {len(num)} números, são eles {num}')

lin('soma')
soma(3, 5)
soma(a=12, b=3)

lin('contador')
contador(2, 4, 8)
contador(1, 6)
contador(3, 7, 9, 2)
