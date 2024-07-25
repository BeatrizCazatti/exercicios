#desafio 05: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se eles podem ou não formar um triângulo.E classifique o triângulo de acordo a medida dos seus lados.

r1 = float(input('reta 1:'))
r2 = float(input('reta 2:'))
r3 = float(input('reta 3:'))

#cola: Só irá existir um triângulo se, somente se, um de seus lados deve ser menor que a soma dos outros dois lados.

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 +r2:
    print('essas retas PODEM FORMAR um triângulo.')
else:
    print('essas retas NÃO PODEM FORMAR um triângulo.')

#CLASSIFICAÇÃO
if r1 == r2 == r3:
    print('equilátero')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('isósceles')
else:
    print('escaleno')