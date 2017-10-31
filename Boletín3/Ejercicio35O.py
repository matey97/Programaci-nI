'''
Created on 12 de nov. de 2015

@author: al341802-Miguel Matey Sanz
'''
from moduloimagen import leerImagen, mostrarImagen

nombreFichero=input('Introduce el nombre de la imagen: ')
matriz=leerImagen(nombreFichero)

c=int(input('Introduce el umbral: '))

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j]>c:
            matriz[i][j]=255
        else:
            matriz[i][j]=0
            
mostrarImagen(matriz)