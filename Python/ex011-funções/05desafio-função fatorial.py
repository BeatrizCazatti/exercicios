#desafio 05: Crie um programa que tenha uma função fatorial() que raceba dois parâmetros: o primeiro que indique o número a calcular a o outro chamado show. que será um valor lógico (opcional) indicando sa será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor fatorial de num.
    """
    result = 1
    
    while num != 0:
        if show:
            print(f' {num} X' if num > 1 else f' {num} = ', end='')
        result *= num
        num -= 1
    return result

print(fatorial(int(input('Digite um número para calcular seu fatorial:')), False))
help(fatorial)