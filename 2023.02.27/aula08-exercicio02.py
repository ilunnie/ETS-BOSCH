
"""
Created on 27/02/2023

@author: Luis Gustavo Caris dos Santos
""""""
    Exercício 2 - Aula 8

Objetivo:
     • Crie uma classe 'Carro';
     • Com atributos e Métodos que descrevem o carro;
     • Ao menos um método e uma propriedade(Atributo) estático;
"""

import random

# Classe para criar os carros
class Carro():
    __quantidade = 0

    def __init__(self, placa, portas : int) -> None:
        Carro.__quantidade += 1
        self.__placa = placa
        self.__portas = portas

    def getPlaca(self):
        return self.__placa

    def getPortas(self):
        return self.__portas

    @staticmethod
    def getQuantidade():
        return Carro.__quantidade

# Cria entre 10 e 1k carros
carros = []
for i in range(random.randint(10, 1000)):
    carros.append(Carro(str(i).zfill(5), random.choice([2, 4])))

print(Carro.getQuantidade())
print(carros[2].getPlaca())
print(carros[2].getPortas())