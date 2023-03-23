
"""
Created on 08/03/2023

@author: Luis Gustavo Caris dos Santos
""""""
    Exercício 1

Desafio:
     • Será que tem alguma relação com a taxa de sobrevivente se ele estava com a família?
"""

# Importa a(as) bibliotecas
import pandas
import os

# Salva o csv na variavel 'titanic'
arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'titanic.csv')
titanic = pandas.read_csv(arquivo, sep=',')

def calcular_porcentagem(val, total):
    percent = float(val/total)
    beautiful_percent = ("%.2f" % (percent * 100) + "%")
    return beautiful_percent

titanic["Relatives"].fillna(0)

mortos = titanic["Survived"][titanic["Survived"] == 0].count()
mortosRelatives = titanic["Relatives"][titanic["Relatives"] > 0].count()
vivos = titanic["Survived"][titanic["Survived"] == 1].count()
vivosRelatives = titanic["Relatives"][titanic["Relatives"] > 1].count()
total = titanic["Survived"].count()

print('\n\n\n')
print(f'{calcular_porcentagem(mortos, total)} morreram, entre eles {calcular_porcentagem(mortosRelatives, mortos)} tinham parentes a bordo')
print(f'{calcular_porcentagem(vivos, total)} sobreviveram, entre eles {calcular_porcentagem(vivosRelatives, vivos)} tinham parentes a bordo')
print('\n\n\n')