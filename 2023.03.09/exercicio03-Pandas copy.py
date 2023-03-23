
"""
Created on 09/03/2023

@author: Luis Gustavo Caris dos Santos
""""""
    Exercício 3

Desafio:
     • Vamos preencher os nulos de maneira que se o passageiro for mulher, esse recebe a idade media das mulheres. Se o passageiro dor homem ele recebe a idade média dos homens
"""

# Importa a(s) biblioteca(s)
import pandas
import os
import matplotlib.pyplot as plt

# Salva o csv na variavel 'titanic'
arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'titanic.csv')
titanic = pandas.read_csv(arquivo, sep=',')

