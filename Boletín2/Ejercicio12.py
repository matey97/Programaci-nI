'''
Created on 8 de oct. de 2015

@author: al341802
'''
gastado=int(input("Introduce la cantidad de kWh consumidos:"))

kwh=0
importe=0

if 0<=gastado<=100:
    importe= gastado*0.05
if 100 <gastado<=250:
    kwh= gastado-100
    importe= 100*0.05 + kwh*0.07
if gastado>=250:
    kwh= gastado-250
    importe= 100*0.05 + 150*0.07 + kwh*0.1
    
print("IMPORTE:{0:.3f} euros".format(importe))
    
    