'''
Created on 22 de oct. de 2015

@author: al341802-Miguel Matey Sanz
'''
n=int(input('Introduce un número entero: '))

print('Los {0} primeros números primos son:'.format(n),end=' ')

veces=1
numero=2

while veces<=n:    
    es_primo=True
    divisor=2
    while divisor<numero and es_primo:
        if numero%divisor==0:
            es_primo=False
        else:
            divisor+=1
    if es_primo:
        print(numero, end=' ')
        veces+=1
    numero+=1