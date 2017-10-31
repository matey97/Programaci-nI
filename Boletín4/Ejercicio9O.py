'''
Created on 19 de nov. de 2015

@author: al341802-Miguel Matey Sanz
'''
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

plantilla=input('Introduce la plantilla de respuestas correctas: ')
print('Ve introducendo respuestas de alumnos, o vacío para acabar...')
respuesta=input('Nuevas respuestas: ')
corregidos=0

while respuesta!='':
    if corregir_test(plantilla, respuesta)==None:
        print('La cadena introducida es de longitud {0} (se esperaba {1})'.format(len(respuesta),len(plantilla)))
    else:
        [bien,mal,ns_nc]=corregir_test(plantilla, respuesta)
        print('Resultados: {0} BIEN; {1} MAL; {2} NS/NC'.format(bien, mal, ns_nc))
        corregidos+=1
    respuesta=input('Nuevas respuestas: ')
    
print('Alumnos corregidos: ', corregidos)    
    