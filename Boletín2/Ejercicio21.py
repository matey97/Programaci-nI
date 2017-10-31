'''
Created on 15 de oct. de 2015

@author: al341802
'''
n=int(input('Introduce un número entero: '))
cuadrado=1
while cuadrado**2<n:
    print('El cuadrado de {0} es {1}.'.format(cuadrado,cuadrado**2))
    cuadrado+=1