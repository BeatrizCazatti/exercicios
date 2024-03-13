import os

def exibir_nome():
    print('''
          𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤
          ''')

def exibir_opções():
    print('1.Cadastrar')
    print('1.Listar')
    print('1.Ativar')
    print('1.Sair')

def finalizar_programa():
    os.system('cls')
    print('end \n')
def escolher_opção():
    opção_escolhida = int(input('\n escolha uma opção:'))

    if opção_escolhida == 1:
        print('primeiro')
    elif opção_escolhida == 2:
        print('segundo')
    elif opção_escolhida == 3:
        print('terceiro')
    else:
        finalizar_programa()  

def main():
    exibir_nome()
    exibir_opções()
    escolher_opção()

if __name__ == '__main__':
    main()