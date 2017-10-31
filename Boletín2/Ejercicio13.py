'''
Created on 8 de oct. de 2015

@author: al341802
'''
from math import ceil, floor
veces=int(input("¿Cuantas veces prevés utilizar el gimnasio? "))

precio_tarjeta=50       #Precios de cada cosa
precio_bono=20
precio_entrada=3

bono=10     #Numero de entradas con cada cosa
entrada=1

con_bonos= ceil(veces/bono)             #Calculo con solo bonos.
con_bonosyentradas= floor(veces/bono)   #Calculo con bonos y tarjetas (numero de bonos)
con_bonosyentradas2= veces%bono         #calculo con bonos y entradas (numero de entradas)

final_bono= con_bonos*precio_bono                                                   #Precio con solo bonos
final_bye= con_bonosyentradas*precio_bono+ con_bonosyentradas2*precio_entrada       #Precio con bonos y entradas

print("Con tarjeta: {0} euros.".format(precio_tarjeta))
print("Con bonos ({0}): {1} euros.".format(con_bonos, final_bono))
print("Con bonos ({0}) y entradas ({1}): {2} euros.".format(con_bonosyentradas, con_bonosyentradas2, final_bye))

menor=precio_tarjeta
                                #Comparacion de mejor opción
if menor>final_bono:
    menor=final_bono
if menor> final_bye:
    menor=final_bye
    
if menor==precio_tarjeta:
    print("Recomendación: Tarjeta.")
if menor==final_bono:
    print("Recomendación: Bonos")
if menor==final_bye:
    print("Recomendación: Bonos y tarjetas.")