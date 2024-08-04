def aumentar(preço, taxa, format=True):
    res = preço + (preço * taxa/100)
    return res if format is False else moeda(preço)

def diminuir(preço, taxa, format=True):
    res = preço - (preço * taxa/100)
    return res if format is False else moeda(preço)

def dobro(preço, format=True):
    res = preço*2
    return res if format is False else moeda(preço)

def metade(preço, format=True):
    res = preço/2
    return res if format is False else moeda(preço)

#01.2: Adapte o código do desafio anterior, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.

def moeda(valor, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')

#01.4: Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como uma função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.

def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31m ERRO: "{entrada}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)



