'''
Created on 29 de oct. de 2015

@author: Usuario- Miguel Matey Sanz
'''
print('Ve introduciendo  cadenas de caracteres, o vacío para acabar...')
cadena=input('Nueva cadena:')
anterior=''

while cadena!='':
    secuencias=0
    anterior=''
    for i in range(len(cadena)):
        if cadena[i]>='0' and cadena[i]<='9' and (anterior<'0' or anterior>'9'):
            secuencias+=1
        anterior=cadena[i]
    print('Secuencias de dígitos encontradas: {0}'.format(secuencias))
    cadena=input('Nueva cadena:')

print('¡Adiós!')