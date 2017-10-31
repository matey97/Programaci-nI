'''
Created on 15 de oct. de 2015

@author: al341802-Miguel Matey Sanz
'''
n=int(input('Introduce un número entero: '))
suma=0

for i in range(1,n+1):
    if n%i==0:
        suma+=i
        
print('La suma de los divisores de {0} es {1}.'.format(n,suma))
        