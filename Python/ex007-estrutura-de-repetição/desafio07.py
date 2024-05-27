#desafio 07:

#A média da idade do grupo
#Qual o nome do homem mais velho
#Quantas mulheres têm menos de 20anos

soma = 0
nomeHomemMaisVelho = ''
idadeHomemMaisVelho = 0
mulherSubVinte = 0

for c in range(0,4):
    print('='*10, c+1 , '='*10)
    nome = input('Nome:')
    idade = int(input('Idade:'))
    sexo = input('Sexo:')
    print('='*23, '\n')

    soma += idade
    
    if sexo == 'F' and idade < 20:
        mulherSubVinte += 1
    if sexo == 'M' and idade > idadeHomemMaisVelho:
        idadeHomemMaisVelho = idade
        nomeHomemMaisVelho = nome

print('A média de idades do grupo é {}'.format(soma/4))
if nomeHomemMaisVelho != '':
    print('O homem mais velho é o {}'.format(nomeHomemMaisVelho))
if mulherSubVinte != 0:
    if mulherSubVinte == 1:
        print('Tem {} mulher com menos de 20'.format(mulherSubVinte))
    else:
        print('Têm {} mulheres com menos de 20'.format(mulherSubVinte))


    