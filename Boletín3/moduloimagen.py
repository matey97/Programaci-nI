# -*- coding: iso-8859-15 -*-
#
# VERSION 1.2 (7-Noviembre-2012)
#
# AYUDA del m�dulo 'moduloimagen'. Define tres funciones, 
# que podemos utilizar de la siguiente forma:
#
# - matriz = leerImagen(nombreFichero). Lee la imagen del fichero
#   indicado y la devuelve como una matriz de enteros. Cada 
#   elemento de la matriz se corresponde con un pixel de la 
#   imagen. 
#
# - id = mostrarImagen(matriz). Se dibuja la imagen en la ventana 
#   gr�fica. La imagen se escala autom�ticamente para ocupar toda
#   la ventana gr�fica. El valor devuelto por la funci�n puede 
#   utilizarse para borrar la imagen con la funci�n que se presenta
#   a continuaci�n.
#
# - borrarImagen(id). Borra la imagen identificada como 'id'.
#
from easycanvas import EasyCanvas

def leerImagen(nombreFichero):
    #lee imagen del fichero tux.txt
    f=open(nombreFichero)
    im1=f.read()
    f.close()
    #convierte datos en matriz
    lin=im1.split('\n')
    mat=[]
    for l in lin:
        if l=='': break
        mat.append(list(map(int,l.split())))
    return mat

def mostrarImagen(mat):
    img=Imagen()
    img.imgdata= mat
    img.run()
    
def _entero2color(n):
    return '#'+('%02x'%n)*3
    
class Imagen(EasyCanvas):
    imgdata=None
    
    def main(self):
        self.easycanvas_configure(title = 'Visualizar Matriz',
                                  background = 'white',
                                  size = (400,400), 
                                  coordinates = (0,0, 1000, 1000))
        id = self.dibujarIm(self.imgdata)
        self.create_text(500, 20, "Pulse una tecla para continuar", 10, "center", "black", "left")
        self.readkey()
        self.borrarIm(id)

 
    def dibujarIm(self,mat):
        filas=len(mat)
        columnas=len(mat[0])
        l=[]
        xx1,yy1,xx2,yy2=self.xinf,self.yinf,self.xsup,self.ysup
        px=0.9*(xx2-xx1)/columnas
        py=0.9*(yy2-yy1)/filas
        xx1+= 0.05*(xx2-xx1)
        for i in range(filas):
            for j in range(columnas):
                if mat[i][j]==-1: 
                    col='#ffff00'
                else:
                    col=_entero2color(mat[i][j])
                x1=xx1+px*j
                y1=yy2-py*(i+1)
                x2=xx1+px*(j+1)
                y2=yy2-py*i
                l.append(self.create_filled_rectangle(x1,y1,x2,y2,col))
        return l
    
    def borrarIm(self,ind):
        list(map(self.erase,ind))

