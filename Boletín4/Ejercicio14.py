'''
Created on 19 de nov. de 2015

@author: Usuario- Miguel Matey Sanz
'''
from moduloimagen import leerImagen, mostrarImagen

nombreFichero=input('Introduce el nombre de la imagen: ')
matriz=leerImagen(nombreFichero)

def crear_matriz(filas,columnas,n):
    matriz=[]
    for i in range(filas):
        matriz.append([n]*columnas)
           
    return matriz
            
def binarizar_imagen(matriz,umbral):
    matriz_nueva=crear_matriz(len(matriz),len(matriz[0]),0)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]>umbral:
                matriz_nueva[i][j]=255
           
    return matriz_nueva

umbral=int(input('Introduce el umbral: '))

mostrarImagen(binarizar_imagen(matriz,umbral))