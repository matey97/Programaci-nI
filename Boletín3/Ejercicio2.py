'''
Created on 29 de oct. de 2015

@author: al341802-Miguel Matey Sanz
'''
cadena=input('Introduce un texto (vacio para acabar): ')
larga=cadena
corta=cadena

if cadena=='':
    print('No se ha introducido texto.')
else:
    while cadena!='':
        if len(cadena)>=len(larga):
            larga=cadena
        elif len(cadena)<=len(corta):
            corta=cadena
        cadena=input('Introduce un texto (vacio para acabar): ')

    print('Última cadena de mínima longitud,{0}: ->{1}<-'.format(len(corta),corta))
    print('Última cadena de máxima longitud,{0}: ->{1}<-'.format(len(larga),larga))