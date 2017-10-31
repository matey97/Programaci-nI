'''
Created on 22 de oct. de 2015

@author: al341802-Miguel Matey Sanz
'''
n=int(input("Introduce un número entero: "))

sumafact=1
factorial=0

while sumafact<=n:
    factorial+=1
    sumafact*=factorial
    
    
print("El número buscado es {0} ({1}! <={2} < {3}!)".format(factorial, factorial-1,n,factorial))