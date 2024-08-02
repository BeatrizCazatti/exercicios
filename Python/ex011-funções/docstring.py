help(print) #Abre a documentação da função print

def contador(i, f, p):
    #A docstring de uma função é feita entre aspas tripla
    """
    -> Faz uma contagem e mostra na tela
    param i: início da contagem
    param f: fim da contagem
    param p: passo da contagem
    return: sem retorno
    Função criada por Beatriz Cazatti
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
        c+=p
    print('FIM!')

help(contador)