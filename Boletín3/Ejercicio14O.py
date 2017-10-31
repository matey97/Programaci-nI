'''
Created on 5 de nov. de 2015

@author: al341802-Miguel Matey Sanz
'''
print('Ve introduciendo numeros enteros positivos, o un numero negativo para acabar...')

l_pares=[]
l_impares=[]
numero=int(input('Nuevo número: '))

while numero>=0:
    if numero%2==0:
        l_pares.append(numero)
    else:
        l_impares.append(numero)
    numero=int(input('Nuevo número: '))
    
print('Numeros pares: ',l_pares)
print('Números impares: ',l_impares)