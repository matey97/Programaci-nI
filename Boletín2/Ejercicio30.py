'''
Created on 15 de oct. de 2015

@author: al341802-Miguel Matey Sanz
'''
n=float(input('Introduce un número: '))

numeros=1
final=0
suma=n
mayor=n
menor=n

while final==0:
    a=float(input('Introduce otro número:'))
    if a<0:
        final=-1
    else:
        suma+=a             #Media
        numeros+=1
        if a>mayor:
            mayor=a
        elif a<menor:
            menor=a
            
print('Media: ',suma/numeros)
print('Mínimo: ',menor)
print('Máximo: ',mayor)
