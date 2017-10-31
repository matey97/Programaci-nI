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
    
cuenta=Cuenta()
cuenta.ingresar(100)
cuenta.reintegrar(20)
print(cuenta.consultar_saldo())