'''
Created on 15 de oct. de 2015

@author: al341802-Miguel Matey Sanz
'''

n=int(input('Introduce un número entero: '))

es_primo=True
for i in range(2, n//2):
    if n%i==0:
        es_primo=False
        break

if es_primo:
    print('Es primo.')
else:
    print('No es primo.')
    