'''
Created on 12 de nov. de 2015

@author: al341802-Miguel Matey Sanz
'''
from modulomatrices import leerMatrizEnteros, mostrarMatriz 

nombreFichero=input('Introduce el nombre de un fichero: ')
matriz=leerMatrizEnteros(nombreFichero)

for j in range(len(matriz[0])):
    suma=0
    for i in range(len(matriz)):
        suma+=matriz[i][j]
    print('La suma de los elementos en la columna {0} es {1}'.format(j,suma))