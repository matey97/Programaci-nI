'''
Created on 15 de oct. de 2015

@author: al341802
'''
a=int(input('Introduce el lado a: '))
b=int(input('Introduce el lado b: '))
c=int(input('Introduce el lado c: '))

while a+b<=c or a+c<=b or b+c<=a:
    print('No es un triangulo.')
    print('')
    a=int(input('Introduce el lado a: '))
    b=int(input('Introduce el lado b: '))
    c=int(input('Introduce el lado c: '))
    
if a==b==c:
    print("Es equilátero.")
    
if a==b!=c or b==c!=a or a==c!=b:
    print("ES isósceles.")
    
if not (a==b or a==c or b==c):
    print("Es escaleno.")


    
    
    