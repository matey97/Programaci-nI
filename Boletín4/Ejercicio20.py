'''
Created on 26 de nov. de 2015

@author: al341802-Miguel Matey Sanz
'''
def es_digito(caracter):
    if caracter>='0' and caracter<='9':
        return True
    return False

def extraer_secuencias_digitos(cadena):
    cadena_digitos=[]
    a=''
    for i in range(len(cadena)):
        if es_digito(cadena[i]):
            a+=cadena[i] 
        else:
            cadena_digitos.append(a)
            a=''
    cadena_digitos.append(a)
    i=0
    while i<(len(cadena_digitos)):
        if cadena_digitos[i]=='':
            del cadena_digitos[i]
        else:
            i+=1
        
    return cadena_digitos
            
    
    
    
cadena=input('Introduce una cadena: ')
print('La lista de secuencias obtenida es {0}'.format(extraer_secuencias_digitos(cadena)))