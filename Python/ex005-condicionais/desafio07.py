#desafio 07: Escreva um programa para aprovar o ampréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador a em quantos anos ele vai pagar.
#Calcula o valor da prestação mensal. Sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input('Valor da casa:'))
anos = float(input('Pretende pagar em quantos anos?'))
salario = float(input('Valor bruto do seu salário?'))

mensalidade = valorCasa / (anos*12)

if mensalidade > salario + 30/100 * salario:
    print('NEGADO')
else:
    print('OK')