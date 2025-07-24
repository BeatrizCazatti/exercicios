import numpy as np

a = np.arange(1, 51)
a = a.reshape(5,10)
print(a)

print()
#primeira linha
print(a[0])

print()
#segundo elemento
print(a[0,1])

print()
#conjunto contínuo de linhas (quadrado de elementos)
print(a[2:5])

print()
#terceira coluna
print(a[:, 2])

print()
#todas as linhas e colunas alternadas (de duas em duas)
print(a[:,::2])

#OBS operador ":" - sintaxe de indexação e fatiamento (slicing). 
    # Significa "todos" quando usado sozinho, ou "de... até..." quando usado com números.
    # A sintaxe completa de fatiamento é start:stop:step