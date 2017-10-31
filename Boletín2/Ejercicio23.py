'''
Created on 15 de oct. de 2015

@author: al341802-Miguel Matey Sanz
'''
n=int(input('Introduce un número entero: '))
suma=0

for i in range(1,n+1):
    if  i%3!=0 and i%5!=0:
        suma+=i
    

print('La suma es ',suma)