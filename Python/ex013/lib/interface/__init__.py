def leiaInt(msg):
    while True:
        try: 
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        except(KeyboardInterrupt):
            print('\033[0;31mERRO! O usuário não digitou nenhum valor.\033[m')
        else:
            return n

def linha(tam):
    print('-'*tam)

def cabeçalho(txt, tam):
    linha(tam)
    print(f'\033[0;36m{txt.center(tam)}\033[m')
    linha(tam)

def menu(lista):
    c = 1
    for item in lista:
        print(f'\033[32m{c}\033[m - \033[33m{item}\033[m')
        c += 1
    linha(35)
    option = leiaInt('\033[0;35m Sua opção: \033[m')
    return option