'''
Created on 29 de oct. de 2015

@author: Usuario- Miguel Matey Sanz
'''
cadenaA=input('Introduce una cadena de caracteres A:')
cadenaB=input('Introduce una cadena de caracteres B:')

if cadenaA=='' and cadenaB=='':
    print('B es sufijo de A')
elif cadenaA=='' and cadenaB!='':
    print('B no es sufijo de A')
elif cadenaA!='' and cadenaB=='':
    print('B es sufijo de A')
elif len(cadenaB)>len(cadenaA):
    print('B no es sufijo de A')
else:
    es_sufijo=True
    for i in (-1,-len(cadenaB)):
        if cadenaA[i]!=cadenaB[i]:
            es_sufijo=False
            break
    if es_sufijo:
        print('B es sufijo de A')
    else:
        print('B no es sufijo de A')
        