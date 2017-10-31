'''
Created on 8 de oct. de 2015

@author: al341802
'''
a=int(input("Introduce el primer número:"))
b=int(input("Introduce el segundo número:"))

minimo=a

if b<minimo:
    minimo=b

print("El número menor es {0}".format(minimo))