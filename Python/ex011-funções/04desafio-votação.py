#desafio 04: Crie um programa que tenha uma função chamada voto() qua vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.

from datetime import datetime
idade = 0

def voto(anoNascimento):
    global idade 
    idade = datetime.now().year - anoNascimento

    if idade < 18:
        return 'NEGADO'
    elif idade >= 18 and idade < 65:
        return 'OBRIGATÓRIO'
    else:
        return 'OPCIONAL'

condition = voto(int(input(f'Ano de Nascimento:')))
print(f'A sua idade é {idade}, então o voto é {condition}.')

