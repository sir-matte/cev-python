# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[1;31mERRO: O SITE NÃO ESTÁ ACESSÍVEL NO MOMENTO.')
else:
    print('\033[1;32mO SITE ESTÁ ACESSÍVEL NO MOMENTO.')
    '''print(site.read())'''
