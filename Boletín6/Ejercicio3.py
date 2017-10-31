'''
Created on 17 de dic. de 2015

@author: al341802-Miguel Matey Sanz
'''
from math import floor
def corregir_test(plantilla, respuestas):
    if len(plantilla)!=len(respuestas):
        return None
    correcto=0
    error=0
    ns_nc=0
    for i in range(len(plantilla)):
        if respuestas[i]=='*':
            ns_nc+=1
        elif plantilla[i]==respuestas[i]:
            correcto+=1
        else:
            error+=1
    return [correcto,error,ns_nc]

fichero=open("test.txt")
plantilla=fichero.readline()
numero_de_preguntas=len(plantilla)
for linea in fichero:
    linea=linea.split("#")
    dni=linea[0]
    respuestas=corregir_test(plantilla, linea[1])
    nota=10*(respuestas[0]-respuestas[1])/numero_de_preguntas
    if nota<0:
        nota=0
    nota=floor(nota)
    print('El alumno con DNI {0} ha obtenido una nota de {1:.2f} puntos.'.format(dni, nota))


fichero.close()