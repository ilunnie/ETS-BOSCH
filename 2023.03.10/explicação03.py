# Importa a(s) biblioteca(s)
import os
import pandas
import numpy as np
import matplotlib.pyplot as plt

# Importa o dataframe
arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'respiradores.csv')
df = pandas.read_csv(arquivo, sep=',')

# Cria a figura e o objeto de eixo
fig, eixo = plt.subplots()

# Cria os gráficos de linha
eixo.bar([i-0.25 for i in range(df.shape[0])], df.PARANA, width= +0.25, label='Paraná', align='edge')
eixo.bar([i+0.25 for i in range(df.shape[0])], df.TOTAL/30, width= -0.25, label='Média do Brasil', align='edge')

# Configuração dos textos
eixo.set_title('Comparação de compras de respiradores entre Paraná e a média do Brasil', color='white')
eixo.tick_params(axis='x', labelcolor='white')
eixo.tick_params(axis='y', labelcolor='white')

# Configuração do grid
eixo.grid(linestyle='dashed')

# Define a legenda
eixo.legend()

# configuração da cor de fundo
eixo.set_facecolor('#1C1C1C')

# Define a cor de fundo do gráfico
fig.set_facecolor('#000000')

# Exibe o gráfico
plt.show()