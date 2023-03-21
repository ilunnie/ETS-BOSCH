# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 15:29:12 2023

@author: Luis Gustavo Caris dos Santos
"""

#(A * X + C) % M

A = 40692
C = 127
M = 400
y = 300

pontos, dentro = [], 0
print('<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">')
print('\t<circle cx="200" cy="200" r="200" fill="orange"/>')
for i in range(50000):
    x = (A * (y+i) + C) % M
    y = (A * (x+i) + C) % M
    print(f'\t<circle cx="{x}" cy="{y}" r="5" fill="red"/>')
    pontos.append((x,y))
    if ((x-200)**2+(y-200)**2 < 40000):
        dentro += 1
print('</svg>')

porcento = (dentro/len(pontos))*4
print(f'\n\n{porcento:.2f}')