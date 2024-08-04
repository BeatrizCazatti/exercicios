#desafio 01:Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
#Faça também um programa que importe essa módulo a use algumas dessas funções.

#01.3: Modifique as funções que foram criadas no desafio 01 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda().

from moeda import aumentar, diminuir, dobro, metade, moeda, leiaDinheiro

valor = leiaDinheiro('Digite um preço: R$')

print(f'O aumento de 10% é {aumentar(valor, 10)}')
print(f'A redução de 13% é {diminuir(valor, 13)}')
print(f'O dobro de {moeda(valor)} é {dobro(valor)}')
print(f'A metade de {moeda(valor)} é {metade(valor)}')


