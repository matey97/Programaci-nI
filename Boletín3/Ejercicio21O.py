'''
Created on 5 de nov. de 2015

@author: al341802-Miguel Matey Sanz
'''
print('Ve introduciendo números enteros, o una cadena vacia para acabar...')

lista=[]

numero=input('Nuevo número: ')
if numero!='':
    minimo=int(numero)



while numero!='':
    lista.append(int(numero))
    if int(numero)<minimo:
        minimo=int(numero)
    numero=input('Nuevo número: ')
    
    
print('Lista leída: ',lista)

for i in range(len(lista)):
    if lista[i]==minimo:
        if lista[0]!=lista[i]:
            aux=lista[0]
            lista[0]=lista[i]
            lista[i]=aux
            
            
print('Lista modificada: ',lista)


    