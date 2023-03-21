
"""
Created on 06/03/2023

@author: Luis Gustavo Caris dos Santos
""""""
    Exercício 4

Desafio:
     • Identifique todos os números impares de um array 3x3 e os substitua por 0
"""

import numpy as np

# cria uma matriz 10x10 de números aleatórios
array = np.random.randint(10, size=10)

# exibe o array
print(array)

# pega todos os impares e substitui por 0
array[array%2 != 0] = 0

# exibe o array final
print(array)