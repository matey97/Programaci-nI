'''
Created on 19 de nov. de 2015

@author: al341802-Miguel Matey Sanz
'''

def contar_divisores(a):
    divisores=2
    for i in range(2,a//2+1):
        if a%i==0:
            divisores+=1
    return divisores

n=int(input('Introduce un número entero: '))

print('El número {0} tiene {1} divisores.'.format(n, contar_divisores(n)))