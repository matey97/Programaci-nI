'''
Created on 1 de oct. de 2015

@author: al341802
'''
from math import pi
radio=float(input("Introduce el radio:"))

area=pi*radio**2
long=2*pi*radio

print("El area es:{0:.2f}".format(area))
print("La longitud de la circunferencia es:{0:.2f}".format(long))