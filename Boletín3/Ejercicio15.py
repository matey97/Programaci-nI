'''
Created on 5 de nov. de 2015

@author: al341802-Miguel Matey Sanz
'''
print('Ve introduciendo números enteros, o una cadena vacía para acabar...')

lista=[]
listacuadrados=[]
numero=input('Nuevo número: ')

while numero!='':
    lista.append(int(numero))
    listacuadrados.append(int(numero)**2)
    numero=input('Nuevo número: ')
    
print('Cuadrados de los números leídos: ',listacuadrados)
print('Números leídos: ',lista)