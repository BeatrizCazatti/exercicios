#desafio 01: Crie um programa que teste se o site Pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('ops')
else:
    print('ok')