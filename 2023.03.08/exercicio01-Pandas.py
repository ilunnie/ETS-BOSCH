
"""
Created on 08/03/2023

@author: Luis Gustavo Caris dos Santos
""""""
    Exercício 1

Desafio:
     • E se quisermos um filtro que retorne os registros com os passageiros da primeira classe que sobreviveram e os passageiros da terceira classe que não sobreviveram
"""

# Importa a(as) bibliotecas
import pandas
import os

# Salva o csv na variavel 'titanic'
arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'titanic.csv')
titanic = pandas.read_csv(arquivo, sep=',')

primeira = titanic["Pclass"] == 1
terceira = titanic["Pclass"] == 3

print(titanic[primeira & (titanic["Survived"] == 1) | 
terceira & (titanic["Survived"] == 0)])