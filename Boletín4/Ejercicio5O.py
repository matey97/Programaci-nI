'''
Created on 19 de nov. de 2015

@author: al341802-Miguel Matey Sanz
'''
def sumar_divisores_propios(n):
    sumatorio=0
    for i in range(1,n):
        if n%i==0:
            sumatorio+=i
    return sumatorio

def es_abundante(n):
    return sumar_divisores_propios(n)>n

n=int(input('Introduce un número entero: '))

i=0
contador=0

print('Los {0} primeros números abundantes son: '.format(n),end='')
while contador<n:
    if es_abundante(i):
        print(i, end=' ')
        contador+=1
    i+=1    