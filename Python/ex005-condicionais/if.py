import os
opção_escolhida = int(input('escolha uma opção:'))

def finalizar_programa():
    os.system('cls')
    print('end \n')
    
if opção_escolhida == 1:
    print('primeiro')
elif opção_escolhida == 2:
    print('segundo')
elif opção_escolhida == 3:
    print('terceiro')
else:
    finalizar_programa()    
