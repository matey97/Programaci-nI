'''
Created on 19 de nov. de 2015

@author: al341802-Miguel Matey Sanz
'''

def es_triangulo(a,b,c):
    return a+b>c and b+c>a and a+c>b

def tipo_triangulo(a,b,c):
    if es_triangulo(a,b,c):
        if a==b==c:
            return "Equilatero"
    
        elif a==b!=c or b==c!=a or a==c!=b:
            return "Isosceles"
        else:
            return "Escaleno"
    else:
        return None
    
a=int(input('Introduce el lado a: '))
b=int(input('Introduce el lado b: '))
c=int(input('Introduce el lado c: '))

print(tipo_triangulo(a,b,c))