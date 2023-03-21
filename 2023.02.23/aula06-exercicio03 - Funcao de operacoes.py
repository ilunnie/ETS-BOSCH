
"""
Created on 23/02/2023

@author: Luis Gustavo Caris dos Santos
"""

import math

def operacoes(num):
    print(format(fatorial(num), ".2f").rstrip("0").rstrip("."))
    print(format(inverso(num), ".2f").rstrip("0").rstrip("."))
    print(format(quadrado(num), ".2f").rstrip("0").rstrip("."))
    print(format(raiz(num), ".2f").rstrip("0").rstrip("."))

def fatorial(num):
    if num == 0:
        return 1
    else:
        return num * fatorial(num-1)

def inverso(num):
    try:
        val = 1/num
    except:
        val = 0
    return val

def quadrado(num):
    try:
        val = 1*num
    except:
        val = 0
    return val

def raiz(num):
    try:
        val = math.sqrt(num)
    except:
        val = 0
    return val

while True:
    entrada = input("Digite um valor: ")
    if entrada.isdigit():
        operacoes(float(entrada))
    else:
        break