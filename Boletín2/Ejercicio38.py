'''
Created on 22 de oct. de 2015

@author: al341802-Miguel Matey Sanz
'''
n=int(input("Introduce un número entero: "))

suma=0
anterior1=1
anterior2=0
veces=1

while suma<n:
    suma=anterior1+anterior2
    anterior2=anterior1
    anterior1=suma
    veces+=1
    
if suma==n:
    print('El número buscado es {0}'.format(veces))
else:
    print('No es un número de Fibonacci.')
    