'''
Created on 17 de dic. de 2015

@author: al341802-Miguel Matey Sanz
'''
fichero=open("test.txt")
digitos=0
letras=0

for linea in fichero:
    for caracter in linea:
        if caracter>="0" and caracter <="9":
            digitos+=1
        elif caracter>="a" and caracter <="z" or caracter>="A" and caracter<="Z":
            letras+=1
fichero.close()

print("En el fichero hay {0} dígitos y {1} letras".format(digitos, letras))    
