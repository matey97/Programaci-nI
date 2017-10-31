'''
Created on 17 de dic. de 2015

@author: al341802-Miguel Matey Sanz
'''
fichero=open("DonQuijote.txt")
mayor=-1

for linea in fichero:
    linea=linea.split()
    for cadena in linea:
        if len(cadena)>mayor:
            mayor=len(cadena)
            candidato=cadena
            
print('La secuencia de caracteres sin espacios más larga es "{0}"'.format(candidato))

fichero.close()