'''
Created on 22 de oct. de 2015

@author: al341802-Miguel Matey Sanz
'''

n=int(input("Introduce un número entero: "))

suma=0
anterior1=1
anterior2=0
veces=2
print('Los',n, 'primeros números de Fibonacci son: 1',end=' ')
while veces<=n:
    suma=anterior1+anterior2
    anterior2=anterior1
    anterior1=suma
    veces+=1
    print(suma, end=' ')
    
    
