
"""
Created on 27/02/2023

@author: Luis Gustavo Caris dos Santos
""""""
    Exercício 3 - Aula 8

Objetivo:
     • Criar uma classe chamada 'Calculadora;
     • Nessa classe, deve possuir funções básicas em forma de métodos;

     • Crie uma 'Calculadora científica';
     • Essa classe deve herdar a primeira classe, adicionando métodos com cálculos mais avançados;
"""

import math

class Calculadora():
    def soma(num1, num2):
        return num1+num2
    def subtração(num1, num2):
        return num1-num2
    def divisão(num1, num2):
        return num1/num2
    def multiplicação(num1, num2):
        return num1*num2

class CalculadoraCientifica(Calculadora):
    @staticmethod
    def pi():
        return math.pi
    @staticmethod
    def raiz(num, raiz=3):
        return pow(num, 1/raiz)

print(CalculadoraCientifica.raiz(27))