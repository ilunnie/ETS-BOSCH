
"""
Created on 09/03/2023

@author: Luis Gustavo Caris dos Santos
""""""
    Exercício 1

Desafio:
     • Agora vamos mudar um pouco, será que tem alguma relação entre a taxa de sobrevivência e a idade
"""

# Importa a(s) biblioteca(s)
import pandas
import os
import matplotlib.pyplot as plt

# Salva o csv na variavel 'titanic'
arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'titanic.csv')
titanic = pandas.read_csv(arquivo, sep=',')

# Cria uma nova coluna no DataFrame indicando a faixa etária de cada passageiro
titanic['Age_group'] = pandas.cut(titanic['Age'], bins=range(0, 100, 10), right=False)

# Faz a média de sobrevivencia entre as faixa etárias
sobrevivencia_por_faixaEtária = titanic.groupby('Age_group')['Survived'].mean()

print(sobrevivencia_por_faixaEtária)

# Cria um gráfico com as informações obtidas
sobrevivencia_por_faixaEtária.plot(kind='bar')
# Relaciona os valores da taxa de sobrevivência (0 = 0% e 1 = 100% de taxa de sobrevivência)
plt.ylim([0, 1])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1], ['0%', '20%', '40%', '60%', '80%', '100%'])
# Cria o texto 'Faixa etária' na parte inferior (eixo x)
plt.xlabel('Faixa etária')
# Cria o texto 'Taxa de sobrevivencia' na esquerda (eixo y)
plt.ylabel('Taxa de sobrevivencia')
plt.show()