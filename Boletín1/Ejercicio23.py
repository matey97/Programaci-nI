'''
Created on 1 de oct. de 2015

@author: al341802
'''
from math import sin
a=int(input("Introduce el primer lado:"))
b=int(input("Introduce el segundo lado:"))
angulo=float(input("Introduce en ángulo (en radianes):"))

area= (a*b*sin(angulo))/2

print("El area del triángulo es:{0:.3f}".format(area))