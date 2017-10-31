'''
Created on 12 de nov. de 2015

@author: al341802-Miguel Matey Sanz
'''
from moduloimagen import leerImagen, mostrarImagen

nombreFichero=input('Introduce el nombre de la imagen: ')
matriz=leerImagen(nombreFichero)

for i in range(len(matriz)):
    for j in range(len(matriz[0])//2):
        aux=matriz[i][j]
        matriz[i][j]=matriz[i][len(matriz[0])-1-j]
        matriz[i][len(matriz[0])-1-j]= aux


mostrarImagen(matriz)

