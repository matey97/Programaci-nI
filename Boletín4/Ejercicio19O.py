'''
Created on 26 de nov. de 2015

@author: al341802-Miguel Matey Sanz
'''
from moduloimagen import leerImagen, mostrarImagen

def girar_derecha(matriz):
    matriz_nueva=crear_matriz(len(matriz[0]),len(matriz),0)
    for fila in range(len(matriz)):
        for col in range(len(matriz[0])):
            matriz_nueva[col][fila]=matriz[-fila-1][col]
    return matriz_nueva
    
def crear_matriz(filas,columnas,n):
    matriz=[]
    for i in range(filas):
        matriz.append([n]*columnas)
    return matriz

nombreFichero=input('Introduce el nombre de la imagen: ')
matriz=leerImagen(nombreFichero)

mostrarImagen(girar_derecha(matriz))
