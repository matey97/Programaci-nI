'''
Created on 17 de dic. de 2015

@author: al341802-Miguel Matey Sanz
'''
def todos_digitos(cadena):
    for elemento in cadena:
        if elemento<'0' or elemento>'9':
            return False
    return True

fichero=open("DonQuijote.txt")

for linea in fichero:
    linea=linea.split()
    for cadena in linea:
        if todos_digitos(cadena):
            print(cadena)
            
fichero.close()