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
mayor=0
numero=0

for i in range(1,n):
    divisores=contar_divisores(i)
    if divisores>=mayor:
        numero=i
        mayor=divisores

print('El número con más divisores es {0} ({1} divisores)'.format(numero,mayor))