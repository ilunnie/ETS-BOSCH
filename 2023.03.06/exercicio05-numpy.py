
"""
Created on 06/03/2023

@author: Luis Gustavo Caris dos Santos
""""""
    Exercício 5

Desafio:
     • Crie um array de 2 linhas e 3 colunas e faça as seguintes operações:
        - Faça um reshape de 3 linhas e 2 colunas;
        - Some a primeira linha por 5;
        - Multiplique a segunda linha por 3;
        - E divida a segunda coluna por 2.
"""

import numpy as np

# Cria uma matriz 10x10 de True
array = np.random.uniform(1, 10, size=(2, 3))

# Exibe o array
print(array)

# Faz o reshape
array = np.reshape(array, (3, 2))

# Soma a primeira linha por 5
array[0] = array[0]+5

# Multiplica a segunda linha por 3
array[1] = array[1]*3

# Divide a terceira linha por 2
array[:1] = array[:1]/2

# Exibe o array
print(array)