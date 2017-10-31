'''
Created on 15 de oct. de 2015

@author: al341802-Miguel Matey Sanz
'''
n=float(input('Introduce un número: '))

if n>=0:
    numeros=1
    final=0
    suma=n
else:
    numeros=0
    final=-1

while final==0:
    a=float(input('Introduce otro número:'))
    if a<0:
        final=-1
    else:
        suma+=a
        numeros+=1
        
if numeros==0:
    print('No se han introducido datos.')
else:
    print('Media: {0}'.format(suma/numeros))
    
    