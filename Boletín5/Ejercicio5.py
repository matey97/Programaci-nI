'''
Created on 3 de dic. de 2015

@author: al341802-Miguel Matey Sanz
'''
from random import randint

class Coche:
    def __init__(self):
        self.posicion=0
        self.velocidad=0
    def acelerar(self,cantidad):
        self.velocidad+=cantidad
    def frenar(self,cantidad):
        self.velocidad-=cantidad
    def actualizar_posicion(self,tiempo):
        self.posicion+=self.velocidad*tiempo
    def consultar_posicion(self):
        return self.posicion

num_coches=int(input('Introduce el número de coches: '))
long_carrera=int(input('Introduce la longitud de la carrera: '))
primero=0
distancia=0
l_coches=[]

for coche in range(num_coches):
    coche=Coche()
    coche.acelerar(60)
    l_coches.append(coche)
    
seguir=''
        
while seguir=='':
    while long_carrera>=distancia:
        for i in range(len(l_coches)):
            coche=l_coches[i]
            cantidad=randint(-5,10)
            coche.acelerar(cantidad)
            coche.actualizar_posicion(1)
            if coche.consultar_posicion()>distancia:
                primero=i
                distancia=coche.consultar_posicion()
            print('Coche {0}: {1} Km'.format(i, coche.consultar_posicion()))
        seguir=input('Pulsa <intro> para el siguiente paso... ')
        
    print('El ganador es el coche',primero)
    break
    
    