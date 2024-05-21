#desafio 06: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcula sau IMC e mostre seu status, de acordo com a tabala abaixo:
#- Abaixo de 18.5: Abaixo do Peso
#- Entre 18.5 g 25: Peso ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade mórbida

#cola: imc = peso / altura(kg e m)

peso = float(input('Quantos quilos você tem?'))
altura = float(input('Qual é a sua altura em metros?'))
imc = peso / altura
print('Seu IMC é {:.1f}'.format(imc))

if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc < 25: 
    print('PESO IDEAL')
elif imc < 30:
    print('SOBREPESO')
elif imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
