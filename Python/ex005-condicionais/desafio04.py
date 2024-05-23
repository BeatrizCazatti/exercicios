#desafio 04: Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

#cola: "anos bissextos seriam os divisíveis por quatro...
#...e a conta incluiu que os anos terminados em 00(divisíveis por 100) só seriam bissextos se o resultado da divisão por 400 fosse exato."


ano = int(input('Digite um ano:'))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))


