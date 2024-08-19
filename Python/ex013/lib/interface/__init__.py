def leiaInt(msg):
    valor = 0
    ok = False

    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = n
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número válido.\033[m')
        if ok:
            break
    return valor

def linha(tam):
    print('-'*tam)

def cabeçalho(txt, tam):
    linha(tam)
    print(f'{txt.center(tam)}')
    linha(tam)

def menu(lista):
    c = 1
    for item in lista:
        print(f'\033[32m{c}\033[m - \033[33m{item}\033[m')
        c += 1