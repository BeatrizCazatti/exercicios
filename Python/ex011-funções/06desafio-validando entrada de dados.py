#desafio 06: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

#Ex: n = leialnt('Digita um n')

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

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')