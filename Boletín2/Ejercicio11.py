'''
Created on 8 de oct. de 2015

@author: al341802
'''
angulo=int(input("Introduce un ángulo (en grados):"))

if angulo==0:
    print("Es un ángulo nulo.")
elif angulo<90:
    print("Es un ángulo agudo.")
elif angulo==90:
    print("Es un ángulo recto.")
elif angulo<180:
    print("Es un ángulo obtuso.")
elif angulo==180:
    print("Es un ángulo llano.")
elif angulo<360:
    print("Es un ángulo concavo.")
elif angulo==360:
    print("Es un ángulo completo.")