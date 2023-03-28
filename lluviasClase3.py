import requests

r = requests.get('https://www.frcon.utn.edu.ar/galileo/downld02.txt')

#print(r.headers)
#print(r.status_code)
#print(r.encoding)
#print(r.content)
texto = r.text
textoc = texto[-55:-51]
print(textoc)