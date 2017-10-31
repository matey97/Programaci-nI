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
    eliminar=int(input('¿De que numero debo eliminar su primera aparición en {0}?'.format(lista)))
    encontrado=False
    for numero in range(len(lista)-1,-1,-1):
        if lista[numero]==eliminar:
            del lista[numero]
            encontrado=True
            break
    if not encontrado:
        print('Número no encontrado.')    



print('La lista ha quedado vacía')  