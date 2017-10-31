'''
Created on 26 de nov. de 2015

@author: al341802-Miguel Matey Sanz
'''
from moduloimagen import leerImagen, mostrarImagen


def difuminar_imagen(matriz, borde):
    matriz_nueva=crear_matriz(len(matriz),len(matriz[0]), borde)
    for fila in range(1,len(matriz)-1):
        for col in range(1,len(matriz[0])-1):
            matriz_nueva[fila][col]=round(promediar_punto(matriz,fila,col))
    return matriz_nueva

def promediar_punto(matriz, n_fila, n_col):
    sumatorio=0
    fila=n_fila-1   #Calculamos la primera fila de nuesta matriz 3x3
    col=n_col-1     #Calculamos la primera columna de nuestra matriz 3x3
    for i in range(fila,fila+3):
        for j in range(col, col+3):
            sumatorio+=matriz[i][j]
    return sumatorio/9

def crear_matriz(filas,columnas,n):
    matriz=[]
    for i in range(filas):
        matriz.append([n]*columnas)
           
    return matriz

nombreFichero=input('Introduce el nombre de la imagen: ')
matriz=leerImagen(nombreFichero)
borde=int(input('Introduce el valor del borde: '))


mostrarImagen(difuminar_imagen(matriz,borde))