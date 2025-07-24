import numpy as np

#arange(start, end, step) = cria sequência com espaçamento fixo (como range)
print(np.arange(1, 20))

print(np.arange(1, 20, 2))

print(np.arange(2, 20, 2))

#np.random.rand() – array com números aleatórios entre 0 e 1
print(np.random.rand(3))

#np.random.randint() – inteiros aleatórios em um intervalo
#print(np.random.randint(5)

#reshape - muda a forma (dimensões) do array
arr = np.arange(1, 101)
a = arr.reshape((10,10))
print(a)

#flatten() ou ravel() – transforma array multidimensional em 1D
#flatten - retorna referência 1D do original
#ravel - faz uma cópia do array original(usa mais memória, porém é mais seguro - para não perder os valores iniciais)

b = a.flatten()
print(b)
