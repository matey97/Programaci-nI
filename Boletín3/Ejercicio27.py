'''
Created on 12 de nov. de 2015

@author: al341802-Miguel Matey Sanz
'''
from modulomatrices import leerMatrizEnteros, mostrarMatriz 

nombreFichero=input('Introduce el nombre de un fichero: ')
matriz=leerMatrizEnteros(nombreFichero)
suma=0
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        suma+=matriz[i][j]
 
print('La suma de todos los elementos en la matriz es ',suma)       