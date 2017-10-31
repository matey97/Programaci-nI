'''
Created on 3 de dic. de 2015

@author: al341802-Miguel Matey Sanz
'''

class Cuenta:
    def __init__(self):
        self.saldo=0
    def ingresar(self,cantidad):
        self.saldo+=cantidad
    def reintegrar(self,cantidad):
        self.saldo-=cantidad
    def consultar_saldo(self):
        return self.saldo
    
print('1) Hacer un ingreso')
print('2) Hacer un reintegro')
print('3) Consultar saldo')
print('4) Salir')
eleccion=input('Introduce la opcion: ')
cuenta=Cuenta()

while eleccion!='4':
    if eleccion=='1':
        cantidad=float(input('Introduce la cantidad que quieres ingresar: '))
        cuenta.ingresar(cantidad)
    elif eleccion=='2':
        cantidad=float(input('Introduce la cantidad que quieres reintegrar:'))
        cuenta.reintegrar(cantidad)
    else:
        print('El saldo acutal es {0} euros'.format(cuenta.consultar_saldo()))
    print('1) Hacer un ingreso')
    print('2) Hacer un reintegro')
    print('3) Consultar saldo')
    print('4) Salir')
    eleccion=input('Introduce la opcion: ')