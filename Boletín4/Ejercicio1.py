'''
Created on 19 de nov. de 2015

@author: al341802-Miguel Matey Sanz
'''
from math import pi

def area_circulo(r):
    return pi*r**2

def longitud_circunferencia(r):
    return 2*pi*r

radio=int(input('Introduce el radio: '))

print('Area: {0:.2f}'.format(area_circulo(radio)))
print('Longitud: {0:.2f}'.format(longitud_circunferencia(radio)))

