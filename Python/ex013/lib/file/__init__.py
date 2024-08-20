def arquivoExiste(arq):
    try:
        open(arq, 'rt')
        open(arq, 'rt').close()
        print('acheii')
    except FileNotFoundError:
        print('não encontrei')
        criarArquivo(arq)

def criarArquivo(arq):
    try:
        open(arq, 'wt+')
        open(arq, 'wt+').close()
        print('criado')
    except:
        print('Algo deu errado na criação.')

def lerArquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<27}{dado[1]:>3} anos')

    finally:
        a.close()
    
def cadastrar(arq, nome, idade):
    if nome == '':
        nome = 'Desconhecido'
    if idade == '':
        idade = 0

    try: 
        open(arq, 'at')
    except: 
        print('ERRO ao abrir o arquivo!')
    else:
        try:
            open(arq, 'at').write(f'{nome};{idade}\n')
        except:
            print('ERRO ao cadastrar uma nova pessoa!')
    finally:
        print(f'Cadastro de {nome} feito com sucesso!')
        open(arq, 'at').close()
    