'''
Created on 26 de nov. de 2015

@author: al341802-Miguel Matey Sanz
'''
def promediar_punto(matriz, n_fila, n_col):
    sumatorio=0
    fila=n_fila-1   #Calculamos la primera fila de nuesta matriz 3x3
    col=n_col-1     #Calculamos la primera columna de nuestra matriz 3x3
    for i in range(fila,fila+3):
        for j in range(col, col+3):
            sumatorio+=matriz[i][j]
    return sumatorio/9

from moduloimagen import leerImagen, mostrarImagen

nombreFichero=input('Introduce el nombre de la imagen: ')
matriz=leerImagen(nombreFichero)
n_fila=int(input('Introduce un número de fila: '))
n_col=int(input('Introduce un número de columna: '))

print('El promedio en torno al punto ({0},{1}) es {2:.2f}'.format(n_fila,n_col,promediar_punto(matriz,n_fila,n_col)))