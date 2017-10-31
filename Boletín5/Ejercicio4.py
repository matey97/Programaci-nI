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
    
print('1) Acelerar.')
print('2) Frenar.')
print('3) Actualizar posicion.')
print('4) Consultar posicion.')
print('5) Salir')

eleccion=input('Introduce la opcion: ')
coche=Coche()

while eleccion!='5':
    if eleccion=='1':
        cantidad=float(input('¿Cuanto quieres acelerar? '))
        coche.acelerar(cantidad)
    elif eleccion=='2':
        cantidad=float(input('¿Cuanto quieres frenar? '))
        coche.frenar(cantidad)
    elif eleccion=='3':
        tiempo=float(input('¿Cuanto tiempo ha pasado? '))
        coche.actualizar_posicion(tiempo)
    else:
        print('La posicion actual es {0} Km.'.format(coche.consultar_posicion()))
    print('1) Acelerar.')
    print('2) Frenar.')
    print('3) Actualizar posicion.')
    print('4) Consultar posicion.')
    print('5) Salir')

    eleccion=input('Introduce la opcion: ')