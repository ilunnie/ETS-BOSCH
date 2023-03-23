
"""
Created on 07/03/2023

@author: Luis Gustavo Caris dos Santos
""""""
    Exercício 3

Desafio:
     • Importe as colunas 'crim' e 'medv' do dataset BostonHousing. Mostre somente as primeiras 14 linhas.
"""

# Importa a(as) bibliotecas
import pandas
import os

# Salva o csv na variavel 'df'
arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'BostonHousing.csv')
df = pandas.read_csv(arquivo, sep=',')

# Lista que define quais colunas devem aparecer
lista = ['crim', 'medv']
# Mostra as 14 primeiras linhas das colunas definidas na lista
print(df[lista].head(14))