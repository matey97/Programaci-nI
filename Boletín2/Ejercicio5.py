'''
Created on 8 de oct. de 2015

@author: al341802
'''
a=int(input("Introduce el lado a:"))
b=int(input("Introduce el lado b:"))
c=int(input("Introduce el lado c:"))

if not (a==b or a==c or b==c):
    print("Es escaleno.")
else:
    print("No es escaleno.")