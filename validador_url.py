import re

url = 'https://bytebank.com/cambio'
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ('A Url não é válida.')

print("A Url é válida.")