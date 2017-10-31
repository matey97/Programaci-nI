'''
Created on 29 de oct. de 2015

@author: al341802-Miguel Matey Sanz
'''
a=int(input('Introduce A: '))
b=int(input('Introduce B: '))

C=str(a)+str(b)
R=C*b
S=int(R)+int(a)

print('C, concatenacion de A y B: {0}'.format(C))
print('R, repeticion de C un numero B de veces: {0}'.format(R))
print('S, suma de los números representados por R y A: {0}'.format(S))