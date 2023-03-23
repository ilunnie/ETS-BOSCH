
"""
Created on 07/03/2023

@author: Luis Gustavo Caris dos Santos
""""""
    Exercício 1

Desafio:
     • Mostre totas as colunas do Dataframe, menos a ultima.
"""

# Importa a(as) bibliotecas
import pandas
import os

# Salva o csv na variavel 'titanic'
arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'titanic.csv')
titanic = pandas.read_csv(arquivo, sep=',')

# Opção 1: cria uma lista com todas as colunas até a penultima
lista = titanic.columns[:-1]
print(titanic[lista].head())

# Opção 2: Define diretamente, atravez do indice, para mostrar todas, menos a ultima coluna
print(titanic.iloc[:,:-1].head())