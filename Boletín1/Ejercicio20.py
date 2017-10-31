'''
Created on 1 de oct. de 2015

@author: al341802
'''
from math import pi

radio=float(input("Introduce el radio:"))

area=pi*radio**2
long=2*pi*radio

print("El área es:{0:7.3f}".format(area))

print("La longitud de la circunferencia es:{0:7.3f}".format(long))