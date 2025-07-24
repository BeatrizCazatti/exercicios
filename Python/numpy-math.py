import numpy as np

a = np.arange(0, 8).reshape(4, 2)
b = np.arange(8, 16).reshape(4, 2)
print(a)
print(b)

#adição
print()
print(a+b)
print(np.add(a, b))

#subtração
print()
print(a-b)
print(np.subtract(a, b))

#multiplicação
print()
print(a*b)
print(np.multiply(a, b))

#divisão
print()
print(a/b)
print(np.divide(a, b))

#multiplicação de matrizes(número de linhas igual ao número de colunas)
print("antes:", b.shape)
b = b.reshape(2, 4)
print("agora:", b.shape)
print(b)

print()
print(a@b)
print(np.dot(a, b))

#max e min
print()
print(a.max())
print(a.argmax())
print(b.min())
print(b.argmin())

#soma todos os elementos
print()
print(a)
print(np.sum(a))
print(np.sum(a, axis=1)) #soma de cada linha
print(np.sum(a, axis=0)) #soma de cada coluna

#média aritmética do array
print()
print(a.mean())
print(np.mean(a, axis=1)) #média por linha
print(np.mean(a, axis=0)) #média por coluna

#raiz quadrada e log
print()
print(np.sqrt(b))
print(np.log(b))