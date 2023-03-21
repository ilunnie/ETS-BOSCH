
"""
Created on 24/02/2023

@author: Luis Gustavo Caris dos Santos
""""""
    Exercício 2 - Aula 7

Título: Manipulando textos

Objetivo:
     • Crie um programa em que o usuário escolhe uma palavra e o programa diz quantas vezes essa palavra aparece em algum arquivo
     • DICA: Utilize as funções split e strip 
"""

import random

alfabeto = "abcdefghijklmnopqrstuvwxyz"

# Abre um arquivo de texto para escrita (modo append)
with open("2023.02.24/letras.txt", "a") as arquivo:
# Adiciona uma letra aleatória no arquivo txt
    for i in range(random.randint(10000, 1000000)):
        arquivo.write(alfabeto[random.randint(0, len(alfabeto) - 1)])

# Inicia o programa
while True:
    # Tenta verificar se a palavra digitada está na frase
    try:
        palavra = input('Digite uma palavra:')
        with open("2023.02.24/letras.txt", "r") as arquivo:
            print(f'A palavra "{palavra}" apareceu {arquivo.read().count(palavra.lower())} vezes no arquivo\n\n\n')
    except KeyboardInterrupt:
        print('\n\n\n\n\nPrograma finalizado')
        break
    except:
        print('\n\n\nAconteceu algum erro, tente novamente')