'''
Created on 19 de nov. de 2015

@author: al341802-Miguel Matey Sanz
'''
def leer_lista_enteros():
    lista=[]
    print('Introduce un numeros enteros, o vacío para acabar...')
    n=input('Nuevo número: ')
    while n!='':
        lista.append(int(n))
        n=input('Nuevo número: ')
    return lista

def borrar_todos(lista, n):
    i=0
    while i<len(lista):
        if lista[i]==n:
            del lista[i]
            i-=1
        i+=1
    return lista

print('Ve introduciendo números enteros, o una cadena vacía para acabar...')

lista=leer_lista_enteros()

while len(lista)!=0:
    n=int(input('De que numero debo eliminar todas sus apariciones en {0} '.format(lista)))
    lista=borrar_todos(lista,n)
    
print('La lista ha quedado vacía')
    
        