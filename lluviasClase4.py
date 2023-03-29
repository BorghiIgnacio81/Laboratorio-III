# capturar la ultima temperatura con el dia y la hora y sacar la diferencia con la fecha actual

import requests
import datetime
r = requests.get('https://www.frcon.utn.edu.ar/galileo/downld02.txt')

#print(r.headers)
#print(r.status_code)
#print(r.encoding)
#print(r.content)
texto = r.text
ahora=str(datetime.datetime.now())

textodia=texto[-250:-238]
textohora=texto[-236:-231]
textoc = texto[-228:-224]

textsolohora=textohora[0:2]
textsolomin=textohora[3:5]
solohora=ahora[11:13]
solomin=ahora[14:16]
print(textsolohora)
print(textsolomin)
print(textohora)
print(textoc)
print(solohora)
print(solomin)
if solohora == textsolohora:
    dif=int(solomin)-int(textsolomin)
    print("En el dia: "+textodia+" a las "+textohora+" la temperatura es de "+textoc+"C°"+"la medicion es de hace "+str(dif)+" minutos exactamente")
else:
    dif=(int(solomin)+10)-(int(textsolomin)-50)
    print (dif)
    print("En el dia: "+textodia+" a las "+textohora+" la temperatura es de "+textoc+"C°"+"la medicion es de hace "+str(dif)+" minutos exactamente")