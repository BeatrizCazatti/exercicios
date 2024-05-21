#imc: quociente do peso pela altura(kg e m)

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
