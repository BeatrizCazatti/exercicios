n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))

s = n1 + n2
m = n1 * n2
d = n1 / n2

r = n1 ** (1/2)
p = n1 ** 2

di = n1 // n2
e = n1 % n2

print('A soma é {}, a multiplicação é {}, e a divisão é {:.3f}'.format(s, m, d))
print('A raiz é {} e potência é {}'.format(r, p))
print('A divisão inteira é {} e oresto é {}'.format(di, e))