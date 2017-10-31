'''
Created on 22 de oct. de 2015

@author: al341802-Miguel Matey Sanz
'''
n=int(input('Introduce un número entero: '))

print('Los números primos menores que {0} son:'.format(n),end=' ')

for numero in range(2,n):
    #comprovar si numero es primo
    es_primo=True
    divisor=2
    while divisor<numero and es_primo:
        if numero%divisor==0:
            es_primo=False
        else:
            divisor+=1
    if es_primo:
        print(numero, end=' ')