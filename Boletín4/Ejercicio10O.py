'''
Created on 19 de nov. de 2015

@author: al341802-Miguel Matey Sanz
'''
def contar_secuencias_digitos(cadena):
    secuencia=0
    if cadena[len(cadena)-1] in '0123456789':
        secuencia+=1
    for i in range(len(cadena)-1):
        if cadena[i] in '0123456789' and cadena[i+1] not in '0123456789':
            secuencia+=1
    return secuencia
            
print('Ve introduciendo cadenas de caracteres, o vacío para acabar...')
cadena=input('Nueva cadena: ')

while cadena!='':
    print('Secuencias de dígitos encontradas: ',contar_secuencias_digitos(cadena))
    cadena=input('Nueva cadena: ')
print('Adiós')    