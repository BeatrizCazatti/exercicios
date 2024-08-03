#desafio 07: Faça um um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando a o manual vai aparecer. Quando o usuário digitar a palavra 'FIM'. o programa sa encerrará.

#OBS: use cores.
c = ('\033[0,0m',     #sem cor
    '\033[0,30, 41m'    #vermelho
    );
    
def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')

def ajuda(com):
    help(com)

def interactiveHelp():
    titulo('SISTEMA', 1)
    while True:
        comando = input('Função ou biblioteca > ').lower() 
        print('...')
        if comando == 'fim':
            break
        else:
            ajuda(comando)

interactiveHelp()