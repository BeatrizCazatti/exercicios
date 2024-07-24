#desafio 14: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano da contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. Considere aposentadoria com 35 anos de contribuição.

from datetime import datetime
pessoas = {}

nome = str(input('Nome: '))
pessoas['nome'] = nome

anoNascimento = int(input('Ano de nascimento: '))
pessoas['idade'] = datetime.now().year - anoNascimento

carteira = int(input('Carteira de Trabalho (0 não tem): '))
pessoas['ctps'] = carteira

if carteira != 0:
    anoContratacao = int(input('Ano de contratação: '))
    pessoas['contratação'] = anoContratacao

    salario = int(input('Salário: '))
    pessoas['salário'] = salario
    pessoas['aposentadoria'] = 35 - (datetime.now().year - anoContratacao)



print('-'*30)
for k, v in pessoas.items():
    print(f'    - {k} tem valor {v}.')
    