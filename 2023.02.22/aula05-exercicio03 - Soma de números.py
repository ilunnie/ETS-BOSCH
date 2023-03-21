
"""
Created on 22/02/2023

@author: Luis Gustavo Caris dos Santos
"""

num, i = int(input("Digite um número:")), 0
valor = num

while i < num:
    valor += i
    i += 1

print("O valor total da soma é", valor)