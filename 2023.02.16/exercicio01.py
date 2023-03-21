# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 13:19:10 2023

@author: Luis Gustavo Caris dos Santos
"""

# pontos = ([10, 10],
#           [20, 7],
#           [20, 2],
#           [0, 2],
#           [0, 7],
#           [30, 7])

pontos = []
for p in range(6):
    pontos.append([])
    pontos[p].append(float(input(f'{p+1}° ponto - Digite o x: ')))
    pontos[p].append(float(input(f'{p+1}° ponto - Digite o y: ')))

for i in range(5):
    if i != 4:
        if ((((pontos[i][0]-pontos[i+1][0])*(pontos[5][1]-pontos[i+1][1]))-((pontos[i][1]-pontos[i+1][1])*(pontos[5][0]-pontos[i+1][0])))>0):
            pontos[i].append(True)
        elif ((((pontos[i][0]-pontos[i+1][0])*(pontos[5][1]-pontos[i+1][1]))-((pontos[i][1]-pontos[i+1][1])*(pontos[5][0]-pontos[i+1][0])))<0):
            pontos[i].append(False)
    else:
        if ((((pontos[i][0]-pontos[0][0])*(pontos[5][1]-pontos[0][1]))-((pontos[i][1]-pontos[0][1])*(pontos[5][0]-pontos[0][0])))>0):
            pontos[i].append(True)
        elif ((((pontos[i][0]-pontos[0][0])*(pontos[5][1]-pontos[0][1]))-((pontos[i][1]-pontos[0][1])*(pontos[5][0]-pontos[0][0])))<0):
            pontos[i].append(False)
    
    if i > 0:
        if (pontos[i][2]) == (pontos[i-1][2]):
            resultado = "dentro"
        else:
            resultado = "fora"
            break
            
print(f"\n\nO 6° ponto esta {resultado}")