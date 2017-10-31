'''
Created on 5 de nov. de 2015

@author: al341802-Miguel Matey Sanz
'''
print('Ve introduciendo números enteros, o una cadena vacía para acabar...')

lista=[]
numero=input('Nuevo número: ')

while numero!='':
    lista.append(int(numero))
    numero=input('Nuevo número: ')
    
print('Ve contestando con números enteros, o con una cadena vacía para acabar...')

suma=input('¿Que número he de buscar en dos posiciones consecutivas? ')

while suma!='':
    for i in range(len(lista)-1):
        if lista[i]+lista[i+1]==int(suma):
            print('{0} + {1} = {2}'.format(lista[i],lista[i+1],suma))
    suma=input('¿Que número he de buscar en dos posiciones consecutivas? ')
        
    
print('¡Adiós!')