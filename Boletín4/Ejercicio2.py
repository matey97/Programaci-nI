'''
Created on 19 de nov. de 2015

@author: al341802-Miguel Matey Sanz
'''
def es_triangulo(a,b,c):
    return a+b>c and b+c>a and a+c>b

a=int(input("Introduce el número a:"))
b=int(input("Introduce el número b:"))
c=int(input("Introduce el número c:"))

print(es_triangulo(a,b,c))