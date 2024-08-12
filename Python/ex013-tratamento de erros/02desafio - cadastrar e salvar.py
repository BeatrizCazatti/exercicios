#desafio 02: Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa ou listar todas.

print('-'*35)
print(f'{"MENU PRINCIPAL":^35}')
print('-'*35)
print('\033[33,44m 1 - \033[m Ver pessoas cadastradas')
print('2 - Cadastrar nova Pessoa')
print('3 - Sair do Sistema')

option = int(input('Opção: '))