'''
Created on 22 de oct. de 2015

@author: al341802-Miguel Matey Sanz
'''
n=int(input('Introduce un número entero: '))

sumafact=1
factorial=0

while sumafact<=n:
    factorial+=1
    sumafact*=factorial
    
factorial-=1
    
print("{0} es factorial de {1}".format(n,factorial))
    
    

    
    