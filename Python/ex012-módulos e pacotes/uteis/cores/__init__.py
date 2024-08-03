c = ('\033[m',    #sem cor
    '\033[31m',   #vermelho
    '\033[32m',   #verde
    '\033[33m',   #amarelo
    '\033[34m'    #azul
    );

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0])