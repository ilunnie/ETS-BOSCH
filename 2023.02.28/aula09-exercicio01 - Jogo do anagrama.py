
"""
Created on 28/02/2023

@author: Luis Gustavo Caris dos Santos
""""""
    Exercício 1 - Aula 9

Objetivo:
     • Crie um programa que desafie o usuário a advinhar a palavra por trás de um anagrama;

Pontuação:
     • O usuário começará com 100 pontos;
     • Será descontado dos pontos cada vez que o usuário errar;
     • Quando 0, deverá aparecer a resposta e que o jogador perdeu;

Palavras:
     • O banco de palavras virá de um txt;
     • A palavra será escolhida aleatoriamente e de acordo com o nível de dificuldade desejado pelo usuário;
     •  A palavra poderá ser embaralhada da maneira desejada.
"""

from random import *

class JogoDoAnagrama():
    def __init__(self, palavras : list, dificuldade : int, vida_inicial : int = 100, desconto : int = 20) -> None:
        self.__resposta = ''
        self.__palavras = palavras
        self.__vidas = vida_inicial
        self.__desconto = desconto
        self.__anagrama = self.__gerarAnagrama(dificuldade)

    # Retorna um anagrama com base na dificuldade
    def __gerarAnagrama(self, dificuldade):
        if dificuldade == 1: # Palavras de 4 a 6 letras
            self.__separarPalavras(randint(4, 6))
        elif dificuldade == 2: # Palavras de 6 a 8 letras
            self.__separarPalavras(randint(6, 8))
        elif dificuldade == 3: # Qualquer palavra
            self.__separarPalavras()

        chars = list(self.__resposta)
        shuffle(chars)
        return ''.join(chars)

    # Busca uma palavra dentro de uma lista que tenha a quantidade de letras definidas
    def __separarPalavras(self, tamanho = None):
        if tamanho == None:
            while len(self.__resposta) < 4:
                self.__resposta = self.__palavras[randint(0, len(self.__palavras)-1)]
        else:
            while len(self.__resposta) != tamanho:
                self.__resposta = self.__palavras[randint(0, len(self.__palavras)-1)]

    def tentar(self, palavra):
        if palavra.upper() == self.__resposta:
            print("Parabéns!\nResposta correta")
            exit()
        else:
            self.__vidas -= self.__desconto
            print('Que pena, você errou...')
    
    def infos(self):
        print(f'vidas: {self.__vidas}')
        print(f'anagrama: {self.__anagrama}')
    
    def getVidas(self):
        return self.__vidas

    def getAnagrama(self):
        return self.__anagrama

    def getResposta(self):
        return self.__resposta

# Passa os itens do txt para uma lista
with open("2023.02.28/Lista-de-Palavras.txt", "r") as arquivo:
    lista = arquivo.read().split()

game = JogoDoAnagrama(lista, int(input("Digite a dificuldade: ")))

while game.getVidas() > 0:
    game.infos()
    game.tentar(input('digite a resposta: '))

print(f'A palavra correta era: {game.getResposta()}')