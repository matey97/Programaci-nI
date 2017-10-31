'''
Created on 19 de nov. de 2015

@author: al341802-Miguel Matey Sanz
'''

def todos_digitos(cadena):
    for elemento in cadena:
        if elemento<'0' or elemento>'9':
            return False
    return True

cadena=input('Introduce una cadena de caracteres: ')

if todos_digitos(cadena):
    print('Todos los caracteres son dígitos.')
else:
    print('No todos los caracteres son dígitos.')
    