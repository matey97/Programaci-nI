'''
Created on 17 de dic. de 2015

@author: al341802-Miguel Matey Sanz
'''
def ordenar_lista(lista):
    for i in range(len(lista)-1):
        menor=lista[i+1]
        for j in range(i+1, len(lista)):
            if lista[j]<menor:
                menor=lista[j]
        for j in range(i+1, len(lista)):
            if menor==lista[j]:
                if lista[j]<lista[i]:
                    aux=lista[i]
                    lista[i]=lista[j]
                    lista[j]=aux
    return lista

fichero=open('test.txt')
dni_txt=open("dni.txt", 'w')
fichero.readline()
dni_l=[]

for linea in fichero:
    linea=linea.split('#')
    dni_l.append(linea[0])
    
dni_ord=ordenar_lista(dni_l)

for dni in dni_ord:
    dni_txt.write('{0}\n'.format(dni))
    
dni_txt.close()
fichero.close()
    