'''
Created on 29 de oct. de 2015

@author: al341802-Miguel Matey Sanz
'''
cadena=input('Introduce un texto (vacio para acabar): ')

while cadena!='':
    print('Su longitud es {0}'.format(len(cadena)))
    cadena=input('Introduce un texto (vacio para acabar): ')
print('¡Adiós!')