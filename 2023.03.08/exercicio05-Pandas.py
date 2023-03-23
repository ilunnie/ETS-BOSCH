
"""
Created on 08/03/2023

@author: Luis Gustavo Caris dos Santos
""""""
    Exercício 1

Desafio:
     • Vamos verificar se a classe cabine (Pclass) também influencia na sobrevivência?
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

primeira = titanic.Survived[titanic["Pclass"] == 1].count()
segunda = titanic.Survived[titanic["Pclass"] == 2].count()
terceira = titanic.Survived[titanic["Pclass"] == 3].count()

mortos1 = titanic.Survived[(titanic["Pclass"] == 1) & (titanic["Survived"] == 0)].count()
mortos2 = titanic.Survived[(titanic["Pclass"] == 2) & (titanic["Survived"] == 0)].count()
mortos3 = titanic.Survived[(titanic["Pclass"] == 3) & (titanic["Survived"] == 0)].count()

sobreviveram1 = titanic.Survived[(titanic["Pclass"] == 1) & (titanic["Survived"] == 1)].count()
sobreviveram2 = titanic.Survived[(titanic["Pclass"] == 2) & (titanic["Survived"] == 1)].count()
sobreviveram3 = titanic.Survived[(titanic["Pclass"] == 3) & (titanic["Survived"] == 1)].count()

print('\n\n\n')
print(f"1° classe: \n   Total: {calcular_porcentagem(primeira, titanic.Survived.count())} \n    Morreram: {calcular_porcentagem(mortos1, primeira)} \n    Sobreviveram: {calcular_porcentagem(sobreviveram1, primeira)}")
print(f"2° classe: \n   Total: {calcular_porcentagem(segunda, titanic.Survived.count())} \n    Morreram: {calcular_porcentagem(mortos2, segunda)} \n    Sobreviveram: {calcular_porcentagem(sobreviveram2, segunda)}")
print(f"3° classe: \n   Total: {calcular_porcentagem(terceira, titanic.Survived.count())} \n    Morreram: {calcular_porcentagem(mortos3, terceira)} \n    Sobreviveram: {calcular_porcentagem(sobreviveram3, terceira)}")
print('\n\n\n')