'''
Created on 19 de nov. de 2015

@author: Usuario- Miguel Matey Sanz
'''
def leer_lista_enteros():
    lista=[]
    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')
    n=input('Nuevo número: ')
    while n!='':
        lista.append(int(n))
        n=input('Nuevo número: ')
    return lista
    
    
def ordenar_lista(lista):
    for i in range(len(lista)-1):
        menor=lista[i+1]
        for j in range(i+1, len(lista)):
            if lista[j]<menor:
                menor=lista[j]
        for j in range(i+1, len(lista)):
            if menor==lista[j]:
                if lista[j]<lista[i]:
                    aux=lista[i]
                    lista[i]=lista[j]
                    lista[j]=aux
    return lista
                    
lista_leida=leer_lista_enteros()
print('Lista leída: ',lista_leida)
lista_ordenada=ordenar_lista(lista_leida)
print('Lista ordenada: ',lista_ordenada)