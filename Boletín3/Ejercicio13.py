'''
Created on 5 de nov. de 2015

@author: al341802-Miguel Matey Sanz
'''
print('Ve introduciendo cadenas de caracteres, o vacio para acabar...')

lista=[]
cadena=input('Nueva cadena: ')

while cadena!='':
    lista.append(cadena)
    cadena=input('Nueva cadena: ')
    
print('Cadenas leídas: ')

for cadena in range(-1, -len(lista)-1, -1):
    print('  Cadena de longitud {0}: -->{1}<--'.format(len(lista[cadena]),lista[cadena]))
    