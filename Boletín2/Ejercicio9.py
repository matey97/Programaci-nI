'''
Created on 8 de oct. de 2015

@author: al341802
'''
a=int(input("Introduce el lado a:"))
b=int(input("Introduce el lado b:"))
c=int(input("Introduce el lado c:"))

if a**2 + b**2 ==c**2 or a**2 + c**2 == b**2 or b**2 + c**2== a**2:
    print("Es un triángulo rectángulo.")
else:
    print("No es un triángulo rectángulo.")