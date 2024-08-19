#desafio 02: Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa ou listar todas.
from lib.interface import *
from lib.file import *
from time import sleep

nomeArquivo = 'listagem.txt'
arquivoExiste(nomeArquivo)
lista = ['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema']

while True:
    cabeçalho('MENU PRINCIPAL', 35)
    resposta = menu(lista)

    sleep(.5)
    if resposta == 1:
        cabeçalho(f'{lista[0]}', 35)
        lerArquivo(nomeArquivo)
    elif resposta == 2:
        cabeçalho(f'{lista[1]}', 35)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema... Até logo!', 35)
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida.\033[m')