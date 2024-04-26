n = int(input('Medida em metros:'))

#m para cm:
print(n,'m = ', n*100, 'cm')

print('{}m corresponde a:'.format(n))

print('{}km \n {}hm \n {}dam \n {}dm \n {}cm \n {}mm'.format(n/1000, n/100, n/10, n*10, n*100, n*1000))
