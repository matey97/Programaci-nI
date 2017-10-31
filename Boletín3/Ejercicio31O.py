'''
Created on 12 de nov. de 2015

@author: al341802-Miguel Matey Sanz
'''
from modulomatrices import leerMatrizEnteros, mostrarMatriz 

nombreFichero=input('Introduce el nombre de un fichero: ')
matriz=leerMatrizEnteros(nombreFichero)

if len(matriz)!=len(matriz[0]):
    print('Error. Se requiere una matriz cuadrada')
else:
    suma=0
    for i in range(len(matriz)):
        suma+=matriz[i][len(matriz[0])-1-i]
    print('La suma de los elementos en la diagonal secundaria es',suma)