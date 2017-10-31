'''
Created on 1 de oct. de 2015

@author: al341802
'''
from math import pi, sin

a=int(input("Introduce el primer lado:"))
b=int(input("Introduce el segundo lado:"))
angulo=float(input("Introduce el ángulo (en grados):"))

radian=(angulo*pi)/180
area=(a*b*sin(radian))/2

print("El área del triángulo es:{0:.3f}".format(area))