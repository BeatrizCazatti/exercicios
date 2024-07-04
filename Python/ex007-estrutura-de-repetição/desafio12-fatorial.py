#desafio 12: Calculadora de fatorial.

num = int(input('Digite um número para calcular seu fatorial:'))
c = num
result = 1
print('{}! ='.format(num), end='')

while c > 0:
    result *= c
    print(' {} '.format(c), end='')
    print('X' if c > 1 else '= {}'.format(result), end='')
    c -= 1




