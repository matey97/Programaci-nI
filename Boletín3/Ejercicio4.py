'''
Created on 29 de oct. de 2015

@author: al341802-Miguel Matey Sanz
'''
cadena=input('Introduce una cadena de caracteres: ')

es_digito=True
indice=0

while indice<len(cadena) and es_digito:
    if cadena[indice]<'0' or cadena[indice]>'9':
        es_digito=False
    indice+=1
    
if es_digito:
    print('Todos los caracteres son dígitos.')
else:
    print('No todos los caracteres son dígitos.')
    