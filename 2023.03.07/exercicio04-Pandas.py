
"""
Created on 07/03/2023

@author: Luis Gustavo Caris dos Santos
""""""
    Exercício 4

Desafio:
     • Uma pessoa quer comprar um carro, e deseja ver as opções mais econômicas. Mostre os dados em um Dataframe com as seguintes condições:
        - Deve ser um carro com 5 lugares (Passengers);
        - Selecione os 10 carros com maior MPG(Miller Per Gallon) na cidade;
        - Dos 10 mais econômicos, mostre os 5 modelos mais baratos(Price);
        - Mostre somente as colunas 'Manufacturer', 'Make', 'Price', 'MPG.city', 'Type', 'Passengers'.
"""

# Importa a(as) bibliotecas
import pandas
import os

# Salva o csv na variavel 'carros'
arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'Cars93_miss.csv')
carros = pandas.read_csv(arquivo, sep=',')[['Manufacturer', 'Make', 'Price', 'MPG.city', 'Type', 'Passengers']]

# Lista que define as colunas que devem ser mostradas
lista = ['Manufacturer', 'Make', 'Price', 'MPG.city', 'Type', 'Passengers']

# Filtra os carros com 5 lugares
filtrados = carros.drop(carros[carros['Passengers'] != 5].index)

# Filtra 10 carros com o maior MPG na cidade
top10MPG = filtrados.sort_values(by='MPG.city', ascending=False).dropna().head(10)

# Mostra os 5 mais baratos entre os filtrados
print(top10MPG[lista].sort_values(by='Price').head(5))