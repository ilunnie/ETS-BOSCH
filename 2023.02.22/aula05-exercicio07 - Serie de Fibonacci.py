
"""
Created on 22/02/2023

@author: Luis Gustavo Caris dos Santos
"""

def sequencia(anterior, atual, quantidade):
    for i in range(quantidade):
        save = anterior
        anterior = atual
        atual += save
        print(atual, end=', ')

while True:
    num = int(input("Escolha a quantidade de números que deseja ver: "))
    anterior, atual = 0, 1
    if (num > 2):
        print(f'{anterior}, {atual}', end=', ')
        sequencia(anterior, atual, num)
    elif (num == 1):
        print(anterior)
    else:
        break
    print('...;')