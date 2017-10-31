'''
Created on 15 de oct. de 2015

@author: al341802-Miguel Matey Sanz
'''

n=int(input('Introduce un número entero: '))
divisores=0

for i in range(1, n+1):
    if n%i==0:
        divisores+=1
        
print('El número {0} tiene {1} divisores.'.format(n, divisores))