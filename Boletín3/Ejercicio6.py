'''
Created on 29 de oct. de 2015

@author: al341802-Miguel Matey Sanz
'''
cadena=input('Introduce una cadena de dígitos: ')
i=int(input('Introduce la primer posicion que visitar: '))
n=int(input('Introduce la longitud deseada: '))


for veces in range(1,n+1):
    print('Paso {0}: visitada posición {1} con contenido {2}.'.format(veces,i,int(cadena[i])))
    i=int(cadena[i])