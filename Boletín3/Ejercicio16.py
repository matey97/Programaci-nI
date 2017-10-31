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
    
while len(lista)>0:
    indice=int(input('¿Qúe posicion debo eliminar de {0}?'.format(lista)))
    if indice<len(lista) and indice>=0:
        del lista[indice]
    else:
        print('Posición incorrecta')

print('La lista ha quedado vacía')
        