'''
Created on 26 de nov. de 2015

@author: al341802-Miguel Matey Sanz
'''
from moduloimagen import leerImagen, mostrarImagen

def reflexion_vertical(matriz):
    for col in range(len(matriz[0])):
        for fila in range(len(matriz)//2):
            aux=matriz[fila][col]
            matriz[fila][col]=matriz[len(matriz)-1-fila][col]
            matriz[len(matriz)-1-fila][col]=aux
    return matriz

nombreFichero=input('Introduce el nombre de la imagen: ')
matriz=leerImagen(nombreFichero)

mostrarImagen(reflexion_vertical(matriz))