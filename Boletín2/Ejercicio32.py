'''
Created on 15 de oct. de 2015

@author: al341802-Miguel Matey Sanz
'''
n=int(input('Introduce un número entero: '))

for numero in range(1,n+1):
    factorial=1
    for i in range(1,numero+1):
        factorial*=i
    print('{0}! = {1}'.format(numero, factorial))
    
