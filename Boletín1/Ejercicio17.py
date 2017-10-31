'''
Created on 1 de oct. de 2015

@author: al341802
'''
from math import sqrt

a=float(input("Introduce a:"))
b=float(input("Introduce b:"))
c=float(input("Introduce c:"))

solucion_a= (-b+sqrt(b**2-4*a*c))/(2*a)
solucion_b= (-b-sqrt(b**2-4*a*c))/(2*a)

print("Las soluciones de la ecuación son: x1= {0:.3f} y x2= {1:.3f}".format(solucion_a,solucion_b))
