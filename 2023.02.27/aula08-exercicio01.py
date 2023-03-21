
"""
Created on 27/02/2023

@author: Luis Gustavo Caris dos Santos
""""""
    Exercício 1 - Aula 8

Objetivo:
     • Crie uma classe 'Casa' parecida com os exemplos acima;
     • Com atributos de Área, Rua, Cor e Nome;
     • Sendo nome opcional na hora de instanciar;
     • Possua um método para mostrar todos os atributos 
"""

class Casa():
    def __init__(self, area, rua, cor, prop = 'Null') -> None:
        self.__area = area
        self.__rua = rua
        self.__cor = cor
        self.__prop = prop
    
    def mostrar(self):
        print(self.__area)
        print(self.__rua)
        print(self.__cor)
        print(self.__prop)