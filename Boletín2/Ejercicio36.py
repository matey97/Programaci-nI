'''
Created on 22 de oct. de 2015

@author: al341802-Miguel Matey Sanz
'''
n=int(input("Introduce un número entero: "))

suma=0
anterior1=1
anterior2=1
veces=3

if n==1:
    print("Fibonacci ({0})= {1}".format(n,n))
elif n==2:    
    print("Fibonacci ({0})= {1}".format(n,1))
else:    
    while veces<=n:
        suma=anterior1+anterior2
        anterior2=anterior1
        anterior1=suma
        veces+=1
    
    print("Fibonacci ({0})= {1}".format(n,suma))