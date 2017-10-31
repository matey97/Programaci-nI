'''
Created on 29 de oct. de 2015

@author: al341802-Miguel Matey Sanz
'''
cadena=input('Introduce una cadena de caracteres: ')

es_digito=True
indice=0
no_digito=""
suma_digitos=0

while indice<len(cadena) and es_digito:
    if cadena[indice]<'0' or cadena[indice]>'9':
        no_digito=cadena[indice]
        es_digito=False
    else:
        suma_digitos+=int(cadena[indice])
    indice+=1
    
if es_digito:
    print('Todos los caracteres son dígitos.')
    print('¿Cuantos dígitos? {0}'.format(len(cadena)))
    print('¿Suma de dígitos? {0}'.format(suma_digitos))
else:
    print('Primer "no dígito": "{0}" en posición {1}'.format(no_digito, indice))
    