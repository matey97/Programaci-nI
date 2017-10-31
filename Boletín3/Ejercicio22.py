'''
Created on 5 de nov. de 2015

@author: Usuario- Miguel Matey Sanz
'''
print('Ve introduciendo números enteros, o una cadena vacia para acabar...')

lista=[]

numero=input('Nuevo número: ')




while numero!='':
    lista.append(int(numero))
    numero=input('Nuevo número: ')
    
    
print('Lista leída: ',lista)

for i in range(len(lista)-1):               #Para cada número...
    minimo=lista[i+1]
    for menor in range(i+1, len(lista)):    #Miro el menor de los que le siguen...
        if lista[menor]<minimo:
            minimo=lista[menor]             #Se el menor, pero no su posición...
    for Min in range(i+1, len(lista)):      #Comparo el menor con cada elemento de la lista posterior a i...
        if lista[Min]==minimo:              #Obtengo posicion del minimo...
            if lista[i]>lista[Min]:
                aux=lista[i]                #Intercambio
                lista[i]=lista[Min]
                lista[Min]=aux
    print('Modificada, tras paso {0}: {1}'.format(i,lista))               
        
                    
print('Lista ordenada: ',lista)
