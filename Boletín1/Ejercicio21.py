'''
Created on 1 de oct. de 2015

@author: al341802
'''
from math import pi

def area_circulo(radio):
    return pi*radio**2

radio=float(input("Introduce el radio:"))

print("El área es:{0:.3f}".format(area_circulo(radio)))
