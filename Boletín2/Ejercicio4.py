'''
Created on 8 de oct. de 2015

@author: al341802
'''
a=int(input("Introduce el lado a:"))
b=int(input("Introduce el lado b:"))
c=int(input("Introduce el lado c:"))

if a==b!=c or b==c!=a or a==c!=b:
    print("ES isósceles.")
else:
    print("No es isósceles.")