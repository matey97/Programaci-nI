'''
Created on 3 de dic. de 2015

@author: al341802-Miguel Matey Sanz
'''

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
    
coche=Coche()
coche.acelerar(100)
coche.actualizar_posicion(2)
coche.frenar(50)
coche.actualizar_posicion(1)
print(coche.consultar_posicion())