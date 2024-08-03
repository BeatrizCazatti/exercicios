from uteis import cores, numeros

cores.titulo('PROCESSANDO...', 2)
valor = int(input('Digite um número: '))
f = numeros.fatorial(valor)
d = numeros.dobro(valor)

print(f'O fatorial de {valor} é {f}')
print(f'E o dobro de {valor} é {d}')