import numpy as np

s1 = 'Meu nome eh Beatriz'
s2 = 'Sou estudante de Ciencia da Computacao'
s3 = 'Graduanda da UERJ, \n Universidade do Estado do RJ'

print(np.char.add(s1, s2))
print(np.char.upper(s1))
print(np.char.lower(s1))
print(np.char.split(s3)) #separa por espaço
print(np.char.splitlines(s3)) #separa por linhas
print(np.char.replace(s3, 'Graduanda da', 'Bacharel pela'))
#print('**********NumPy**********')
print(np.char.center('NumPy',25, '*'))