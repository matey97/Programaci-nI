'''
Created on 5 de nov. de 2015

@author: Usuario- Miguel Matey Sanz
'''
print('Ve introduciendo candidaturas, o vacío para acabar...')

Lcandidatura=[]
Lvotos=[]
totalvotos=0
candidatura=input('Nueva candidatura: ')

while candidatura!='':
    Lcandidatura.append(candidatura)
    candidatura=input('Nueva candidatura: ')
    
for electo in Lcandidatura:
    votos=int(input('Votos para {0}: '.format(electo)))
    Lvotos.append(votos)
    totalvotos+=votos

for partido in range(len(Lcandidatura)):
    print('   {0:.2f}% de los votos a candidaturas para {1}'.format(Lvotos[partido]/totalvotos*100,Lcandidatura[partido]))
    

    