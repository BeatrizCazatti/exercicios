#desafio 07: Faça um um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando a o manual vai aparecer. Quando o usuário digitar a palavra 'FIM'. o programa sa encerrará.

#OBS: use cores.
c = ('\033[m',    #sem cor
    '\033[31m',   #vermelho
    '\033[32m',   #verde
    '\033[33m',   #amarelo
    '\033[34m'    #azul
    );

def titulo(msg, cor):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0])

def ajuda(com):
    help(com)

def interactiveHelp():
    titulo('SISTEMA DE AJUDA DO PYTHON', 3)
    while True:
        comando = input('Função ou biblioteca > ').lower() 
        if comando == 'fim':
            titulo('FINALIZANDO PROGRAMA', 1)
            break
        else:
            titulo('CARREGANDO INFORMAÇÕES...', 2)
            ajuda(comando)

interactiveHelp()