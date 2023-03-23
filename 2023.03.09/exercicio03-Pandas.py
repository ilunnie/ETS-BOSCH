
"""
Created on 09/03/2023

@author: Luis Gustavo Caris dos Santos
""""""
    Exercício 3

Desafio:
     • Vamos fazer o agrupamento por cabine somando as idades usando o apply
"""

# Importa a(s) biblioteca(s)
import pandas
import os
import matplotlib.pyplot as plt

# Salva o csv na variavel 'titanic'
arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'titanic.csv')
titanic = pandas.read_csv(arquivo, sep=',')

def somar_idades_cabine(registros_agrupados):
    return registros_agrupados["Age"].sum()

group = titanic.groupby("Cabin").apply(somar_idades_cabine)
print(group.describe())