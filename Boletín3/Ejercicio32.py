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
        for j in range(i+1, len(matriz[0])):        #Cuando fila es 1, se deberan coger los numeros a partir de i+1
            suma+=matriz[i][j]
    print('La suma de los elementos por encima de la diagonal principal es',suma)
        