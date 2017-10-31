'''
Created on 8 de oct. de 2015

@author: al341802
'''
a=int(input("Introduce el número a:"))
b=int(input("Introduce el número b:"))
c=int(input("Introduce el número c:"))

if a+b>c and a+c>b and b+c>a:
    print("Es un triángulo.")
else:
    print("No es un triángulo.")