'''
Created on 29 de oct. de 2015

@author: al341802-Miguel Matey Sanz
'''
cadena=input('Introduce una cadena de caracteres: ')
new_cadena=""
final_cadena=""
if cadena[0]!=" ":
    new_cadena+=cadena[0]
    
for i in range(1,len(cadena)):
    if cadena[i]!=" ":    
        new_cadena+=cadena[i]
    elif cadena[i-1]!=" ": 
        new_cadena+=cadena[i]
        
if new_cadena[-1]==" ":
    for i in range(-len(new_cadena),-1):
        final_cadena+=new_cadena[i]
    print('Cadena limpiada: ->{0}<-'.format(final_cadena))
   
    
else:    
    print('Cadena limpiada: ->{0}<-'.format(new_cadena))
 
print('Cadena original: ->{0}<-'.format(cadena))   