'''
Created on 6 de nov. de 2015

@author: Usuario- Miguel Matey Sanz
'''
print('Ve introduciendo números enteros, o una cadena vacía para acabar...')

lista=[]
copia=[]
suma=0
numero=input('Nuevo número: ')

while numero!='':
    lista.append(int(numero))
    numero=input('Nuevo número: ')

for num in range(len(lista)-1):
    for i in range(num+1, len(lista)):
        if lista[i]==lista[num] and lista[i] not in copia:
            copia.append(lista[num])
            
for repetido in copia:
    suma+=repetido            
 
print('Números leídos mas de una vez (suman {0}): {1}'.format(suma, copia))
print('Todos los números leídos: {0}'.format(lista))   