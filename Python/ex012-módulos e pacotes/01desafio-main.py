#desafio 01:Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
#Faça também um programa que importe essa módulo a use algumas dessas funções.

#01.3: Modifique as funções que foram criadas no desafio 01 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda().

import moeda
valor = int(input('Digite um preço: '))

print(f'O aumento de 10% é {moeda.aumentar(valor, 10)}')
print(f'A redução de 13% é {moeda.diminuir(valor, 13)}')
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f'A metade de {valor} é {moeda.metade(valor)}')


