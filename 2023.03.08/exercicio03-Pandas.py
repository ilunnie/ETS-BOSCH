
"""
Created on 08/03/2023

@author: Luis Gustavo Caris dos Santos
""""""
    Exercício 1

Desafio:
     • Cria uma nova coluna("Relatives")
"""

# Importa a(as) bibliotecas
import pandas
import os

# Salva o csv na variavel 'titanic'
arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'titanic.csv')
titanic = pandas.read_csv(arquivo, sep=',')

def soma_sibsp_parch(linha):
    return linha["SibSp"] + linha["Parch"]


nova_coluna = titanic.apply(soma_sibsp_parch, axis=1)

titanic["Relatives"] = nova_coluna

print(titanic.head())

# titanic.pop("Relatives")

# print(titanic.head())

titanic.to_csv(arquivo, index=False)