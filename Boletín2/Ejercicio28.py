'''
Created on 15 de oct. de 2015

@author: al341802-Miguel Matey Sanz
'''
n=float(input('Introduce un número: '))
mayor=n
fin=1

while fin==1:
    a=float(input('Introduce un otro número:'))
    if a<0:
        fin=0
    elif a>mayor :
        mayor=a
        
print('Máximo: ',mayor)
        