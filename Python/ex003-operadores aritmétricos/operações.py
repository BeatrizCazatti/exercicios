n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))

s = n1 + n2
m = n1 * n2
d = n1 / n2

di = n1 // n2
e = n1 ** n2

print('A soma é {}, a multiplicação é {}, e a divisão é {:.3f}'.format(s, m, d))
print('A divisão inteira é {} e oresto é {}'.format(di, e))