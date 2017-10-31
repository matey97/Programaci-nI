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
        suma+=matriz[i][i]
    print('La suma de los elementos de la diagonal principal es ', suma)