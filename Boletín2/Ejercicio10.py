'''
Created on 8 de oct. de 2015

@author: al341802
'''
a=int(input("Introduce el primer número:"))
b=int(input("Introduce el segundo número:"))

if a<0 and b<0 or a>0 and b>0:
    print("Su producto es positivo.")
elif a<0 and b>0 or a>0 and b<0:
    print("Su producto es negativo.")
elif a==0 or b==0:
    print ("Su producto es nulo.")