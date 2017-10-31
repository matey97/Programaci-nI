'''
Created on 19 de nov. de 2015

@author: Usuario- Miguel Matey Sanz
'''
from modulomatrices import leerMatrizEnteros, mostrarMatriz 

nombreFichero=input('Introduce el nombre de un fichero: ')
matriz=leerMatrizEnteros(nombreFichero)


def sumar_diagonal_principal(matriz):
    if len(matriz)!=len(matriz[0]):
        return None
    else:
        sumatorio=0
        for i in range(len(matriz)):
            sumatorio+=matriz[i][i]
        return sumatorio

resultado=sumar_diagonal_principal(matriz)
if resultado==None:
    print('Error. Se requiere una matriz cuadrada.')
else:
    print('La suma de los elementos de la diagonal principal es',resultado)