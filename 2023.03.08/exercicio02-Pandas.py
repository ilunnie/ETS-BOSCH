
"""
Created on 08/03/2023

@author: Luis Gustavo Caris dos Santos
""""""
    Exercício 1

Desafio:
     • Robin está procurando por uma mulher que conheceu durante um evento no Titanic, poucas horas antes da tragédia. Ele gostaria de saber se ela sobreviveu e nós podemos ajudar ele através do nosso banco de dados. As informações que ele sabe sobre ela são:
        - Ela embarcou em Southampton (Inglaterra)
        - Ela era da segunda classe
        - Ela tinha 29.0 anos
        - e no nome completo dela tinha Anne, mas ele não sabe se era nome ou sobrenome
"""

# Importa a(as) bibliotecas
import pandas
import os

# Salva o csv na variavel 'titanic'
arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'titanic.csv')
titanic = pandas.read_csv(arquivo, sep=',')

# Preenche os valores vazios
titanic["Name"].fillna('Anne')
titanic["Age"].fillna(29.0)

# Encontra a(s) pessoas que se encaixam na descrição
ela = titanic[titanic["Name"].str.contains("Anne") & (titanic["Age"] == 29) & (titanic["Pclass"] == 2) & (titanic["Embarked"] == 'S')]

# Mostra o nome, idade, classe e local de embarque da(a) pessoa(s)
print(ela[['Name', 'Age', 'Pclass', 'Embarked']])