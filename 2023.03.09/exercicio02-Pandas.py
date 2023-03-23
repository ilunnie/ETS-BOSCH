
"""
Created on 09/03/2023

@author: Luis Gustavo Caris dos Santos
""""""
    Exercício 2

Desafio:
     • Uma técnica muito usada é trocar o valor dos dados númericos é usar a média
     • Vamos preencher os valores de idade nulo com a médias das idades
"""

# Importa a(s) biblioteca(s)
import pandas
import os
import matplotlib.pyplot as plt

# Salva o csv na variavel 'titanic'
arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'titanic.csv')
titanic = pandas.read_csv(arquivo, sep=',')

media = titanic['Age'].mean()
titanic["Age"].fillna(media)