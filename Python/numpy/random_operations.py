import numpy as np

print(np.random.rand(3,1)) #array de 3 elementos com valores aleatórios naturais menores que 1
print(np.random.randn(2,2)) #randn - menores que 1(inclui negativos)
print(np.random.randint(1, 5)) #valor aleatório em determinado intervalo [1, 5[
print(np.random.randint(1, 10, (3,4,5))) #array 3D aleatório no intervalo [1,10[
arr = np.arange(1,10)
print(np.random.choice(arr)) #escolhe um valor de arr