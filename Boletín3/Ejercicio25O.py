'''
Created on 6 de nov. de 2015

@author: Usuario- Miguel Matey Sanz
'''
print('Ve introduciendo alturas sobre el nivel del mar, o una cadena vacía para acabar...')

lista_alturas=[]
lista_desniveles=[]
kilometro=0
maximo=0
altura=input('Altura en metros en el punto kilométrico {0}: '.format(kilometro))

while altura!='':
    lista_alturas.append(int(altura))
    kilometro+=1
    altura=input('Altura en metros en el punto kilométrico {0}: '.format(kilometro))

if len(lista_alturas)<=1:
    print('Recorrido no valido con menos de dos puntos.')
else:    
    for i in range(len(lista_alturas)-1):
        desnivel=lista_alturas[i+1]-lista_alturas[i]
        lista_desniveles.append(desnivel)



    for j in range(len(lista_desniveles)):
        if maximo<lista_desniveles[j]:
            maximo=lista_desniveles[j]
        
    for j in range(len(lista_desniveles)):
        if lista_desniveles[j]==maximo:
            aux=j
            
    print('Lista alturas: {0}'.format(lista_alturas))
    print('Lista desniveles: {0}'.format(lista_desniveles))
       
        
   
    if maximo<=0:
        print('Ningun kilómetro es de subida.') 
    else:      
        print('Kilómetro con mayor desnivel de subida:')
        print('  Entre los puntos kilómetricos {0} y {1}'.format(aux, aux+1))
        print('  Desnivel de {0} m'.format(maximo))
    
   
    