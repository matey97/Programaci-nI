'''
Created on 19 de nov. de 2015

@author: Usuario- Miguel Matey Sanz
'''
from moduloimagen import leerImagen, mostrarImagen

nombreFichero=input('Introduce el nombre de la imagen: ')
matriz=leerImagen(nombreFichero)

def reflexion_horizontal(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])//2):
            aux=matriz[i][j]
            matriz[i][j]=matriz[i][len(matriz[0])-1-j]
            matriz[i][len(matriz[0])-1-j]=aux
    return matriz


mostrarImagen(reflexion_horizontal(matriz))