# Importa a(s) biblioteca(s)
import os
import pandas
import matplotlib.pyplot as plt

# Importa o dataframe
arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'respiradores.csv')
df = pandas.read_csv(arquivo, sep=',')

# Cria a figura e o objeto de eixo
fig, eixo = plt.subplots(nrows=2, ncols=2, figsize=(10,10))

# Define o espaço height entre ps graficos
fig.subplots_adjust(hspace=0.75)

# Cria os gráficos de linha
eixo[0][0].bar(df.MES, df.TOTAL)
eixo[0][1].bar(df.columns[1:-1], df.sum()[1:-1])
eixo[1][0].scatter(df.MES, df['GOIAS'], label="Goiás")
eixo[1][1].plot(df.MES, df.PARANA, color='purple', marker='x', linewidth=3)

titulos = [["COMPRA DE RESPIRADORES POR MÊS", "COMPRA DE RESPIRADORES POR MÊS NOS ESTADOS"], ["COMPRA DE RESPIRADORES POR MÊS EM GOIÁS", "COMPRA DE RESPIRADORES POR MÊS NO PARANÁ"]]

# Define os eixos
for i in range(0, 2, 1):
    for j in range(0, 2, 1):
        # Configuração do titulo
        eixo[i][j].set_title(titulos[i][j], color='white')
        # Configuração das cores
        eixo[i][j].tick_params(axis='x', labelcolor='white', rotation=45)
        eixo[i][j].tick_params(axis='y', labelcolor='white', rotation=45)
        # Configuração do grid
        eixo[i][j].grid(linestyle='dashed')
        # configuração da cor de fundo
        eixo[i][j].set_facecolor('#1C1C1C')

eixo[0][1].tick_params(rotation=90)

# Define a cor de fundo do gráfico
fig.set_facecolor('#000000')

# Exibe o gráfico
plt.show()