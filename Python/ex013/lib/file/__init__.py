def arquivoExiste(nome):
    try:
        open(nome, 'rt')
        open(nome, 'rt').close()
        print('acheii')
    except FileNotFoundError:
        print('não encontrei')
        criarArquivo(nome)

def criarArquivo(nome):
    try:
        open(nome, 'wt+')
        open(nome, 'wt+').close()
        print('criado')
    except:
        print('Algo deu errado na criação.')

def lerArquivo(nome):
    try:
        open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(open(nome, 'rt').read())    