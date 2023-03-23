# Importa a(s) biblioteca(s)
import os
import pandas
import matplotlib.pyplot as plt

# Importa o dataframe
arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'respiradores.csv')
df = pandas.read_csv(arquivo, sep=',')

# Separa as regiões
estados_do_norte = df.loc[:,['AMAZONAS', 'RORAIMA', 'AMAPA', 'PARA', 'TOCANTINS', 'RONDONIA', 'ACRE']]
estados_do_nordeste = df.loc[:,['MARANHÃO', 'PIAUI', 'CEARA', 'RIO GRANDE DO NORTE', 'PERNAMBUCO', 'PARAIBA', 'SERGIPE', 'ALAGOAS', 'BAHIA']]
estados_do_centro_oeste = df.loc[:, ['MATO GROSSO ', 'MATO GROSSO DO SUL', 'GOIAS']]
estados_do_sudeste = df.loc[:, ['SÃO PAULO', 'RIO DE JANEIRO', 'ESPIRITO SANTO ', 'MINAS GERAIS']]
estados_do_sul = df.loc[:,['PARANA', 'SANTA CATARINA', 'RIO GRANDE DO SUL ']]
estados_do_brasil = df.iloc[:,1:-1]

# Cria a figura e o objeto de eixo
fig, eixo = plt.subplots(nrows=2, ncols=3, figsize=(10,10))

# Cria os gráficos de pizza
p1, tx, autotexts = eixo[0][0].pie(estados_do_norte.sum(), labels=None, autopct="", shadow=True)
p2, tx, autotexts = eixo[0][1].pie(estados_do_nordeste.sum(), labels=None, autopct="", shadow=True)
p3, tx, autotexts = eixo[0][2].pie(estados_do_centro_oeste.sum(), labels=None, autopct="", shadow=True)
p4, tx, autotexts = eixo[1][0].pie(estados_do_sudeste.sum(), labels=None, autopct="", shadow=True)
p5, tx, autotexts = eixo[1][1].pie(estados_do_sul.sum(), labels=None, autopct="", shadow=True)
p6, tx, autotexts = eixo[1][2].pie(estados_do_brasil.sum(), labels=None, autopct="", shadow=True)

# Define as legendas
legenda = ['AMAZONAS', 'RORAIMA', 'AMAPA', 'PARA', 'TOCANTINS', 'RONDONIA', 'ACRE']

# Adiciona a legenda
eixo[0][0].legend(p1, legenda, title='Estados do Norte', loc='center left', fontsize=10, bbox_to_anchor=(1.1, 0.5))
eixo[0][1].legend(p2, legenda, title='Estados do Nordeste', loc='center left', fontsize=10, bbox_to_anchor=(1.1, 0.5))
eixo[0][2].legend(p3, legenda, title='Estados do Centro-Oeste', loc='center left', fontsize=10, bbox_to_anchor=(1.1, 0.5))
eixo[1][0].legend(p4, estados_do_sudeste.columns, title='Estados do Sudeste', loc='center left', fontsize=10, bbox_to_anchor=(1.1, 0.5))
eixo[1][1].legend(p5, estados_do_sul.columns, title='Estados do Sul', loc='center left', fontsize=10, bbox_to_anchor=(1.1, 0.5))
eixo[1][2].legend(p6, estados_do_brasil.columns, title='Estados do Brasil', loc='center left', fontsize=7.5, bbox_to_anchor=(1.1, 0.5))

# Ajusta o layout dos subplots
fig.tight_layout()

# Exibe o gráfico
plt.show()

