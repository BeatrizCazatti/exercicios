import numpy as np

#ndarray = 
lista = [1,2,3,4,5]
print('1D Array')
array_1d = np.array(lista)
print(array_1d,'\n')

matriz = [[1,2,3], [4,5,6]]
print('2D Array')
array_2d = np.array(matriz)
print(array_2d,'\n')

tridimensional = [[1,2,3], [4,5,6], [7,8,9]]
print('3D Array')
array_3d = np.array(tridimensional)
print(array_3d,'\n')

#type = tipo da variável
print(type(array_2d))

print()
#size = numero de elementos do array
print(array_1d.size)
print(array_2d.size)
print(array_3d.size)

print()
#shape = numero de linhas e colunas
print(array_1d.shape)
print(array_2d.shape)
print(array_3d.shape)

print()
#dtype = tipo de dados de cada array
print(array_1d.dtype)
print(array_2d.dtype)
print(array_3d.dtype)

print()
#transpose = gera a transposta do array(troca linhas por colunas)
#array_2d.transpose()
print(array_1d.transpose())
print()
print(array_2d.transpose())
print()
print(array_3d.transpose())


print()
#criação de arrays
vazio_3x3 = np.empty((3,3))
print(vazio_3x3)
vazio_3x3 = np.empty((3,3), dtype = int)
print(vazio_3x3)

print()
zeros_3x3 = np.zeros((3,3))
print(zeros_3x3)

print()
a = np.ones((3,3))
print(a)
print()
b = np.ones((3,3),  dtype = int)
print(b)

print()

c = np.ones((4), dtype = str)
print(c)
c = np.zeros((4), dtype = str)
print(c)

d = np.ones((4), dtype = bool)
print(d)
d = np.zeros((4), dtype = bool)
print(d)