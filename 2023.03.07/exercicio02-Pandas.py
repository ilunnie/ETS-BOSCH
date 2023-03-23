
"""
Created on 07/03/2023

@author: Luis Gustavo Caris dos Santos
""""""
    Exercício 2

Desafio:
     • E se quisermos um Dataframe com a descrição apenas das colunas 'Age' e 'Pclass'?
"""

# Importa a(as) bibliotecas
import pandas
import os

# Salva o csv na variavel 'titanic'
arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'titanic.csv')
titanic = pandas.read_csv(arquivo, sep=',')

# Cria a lista contendo as colunas que deve ser descrita
lista = ['Age', 'Pclass']
# Mostra o .describe das colunas expecificadas na lista
print(titanic[lista].describe())