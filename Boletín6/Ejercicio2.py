'''
Created on 17 de dic. de 2015

@author: al341802-Miguel Matey Sanz
'''
fichero=open("test.txt")

for linea in fichero:
    es_alumno=False
    for caracter in linea:
        if caracter == "#":
            es_alumno=True
            break
    if es_alumno:
        linea=linea.split("#")
        dni=linea[0]
        respuesta=linea[1]
        print('El alumno con DNI {0} ha respondido {1}'.format(dni,respuesta), end='')
    
fichero.close()