'''
Created on 29 de oct. de 2015

@author: al341802-Miguel Matey Sanz
'''
print('Ve introduciendo palabras o vacío para acabar...')
palabra=input('Nueva palabra:')
no_correcta=""

while palabra!="":
    es_correcta=True
    for i in range(len(palabra)):
        if (palabra[i]<'A' or palabra[i]>'z') and palabra[i] not in 'ñáéíóúü':
            es_correcta=False
            no_correcta=palabra[i]
            print('Contiene un caracter que no es del alfabeto castellano: "{0}"'.format(no_correcta))
            break
    if es_correcta:
        print('Podría ser una palabra correcta.')
    palabra=input('Nueva palabra:')
    
print('¡Adiós!')