#desafio 02: Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa ou listar todas.
from lib.interface import *

cabeçalho('MENU PRINCIPAL', 35)

lista = ['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema']
menu(lista)

option = int(input('Opção: '))