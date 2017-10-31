'''
Created on 8 de oct. de 2015

@author: al341802
'''
importe=float(input("Introduce el importe de la compra: "))
zona=input("Introduce la zona de envío (A/B/C): ").upper()
socio=input("¿Eres socio (S/N)? ").upper()
envio=0
coste=0

if importe<=150:
    if socio=='S':
        envio=19
    else:
        envio=25
elif importe <=750:
    if socio=='S':
        envio=49
    else:
        envio=60
elif importe <= 1500:
    if socio=='S':
        envio=89
    else:
        envio=120        
else:
    if socio=='S':
        envio= (importe*6)/100
    else:
        envio= (importe*8)/100

if zona=='A':
    coste=envio
elif zona=='B':
    coste=envio+30
else:
    coste=envio+69
    
print("Gastos de envio:{0:.2f} euros.".format(coste))