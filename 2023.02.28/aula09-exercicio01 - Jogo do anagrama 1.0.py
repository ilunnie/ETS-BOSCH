
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

import tkinter as tk
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
            return True
        else:
            self.__vidas -= self.__desconto
            return False
    
    def infos(self):
        print(f'vidas: {self.__vidas}')
        print(f'anagrama: {self.__anagrama}')
    
    def getVidas(self):
        return self.__vidas

    def getAnagrama(self):
        return self.__anagrama

    def getResposta(self):
        return self.__resposta

class Janela:
    def __init__(self, master, JogoDoAnagrama, lista, dificuldade, vida_inicial, queda):
        self.master = master
        self.jogo = JogoDoAnagrama(lista, dificuldade, vida_inicial, queda)
        self.jogo.infos()
        self.master.title("Jogo do Anagrama") # Define o nome da janela
        self.master.geometry("200x150") # Define o tamanho da janela
        self.master.resizable(False, False) # Deixa a janela fixa

        # Testo do anagrama
        self.label = tk.Label(master, text=self.jogo.getAnagrama(), font=("Arial", 14, "bold"))
        self.label.pack(pady=15)

        # Configurações da entrada de texto
        self.entrada = tk.Entry(master)
        self.entrada.bind("<Return>", self.processar_palpite) # Chama a função quando o usuário apertar Enter
        self.entrada.pack(pady=5)

        # Área de vidas
        self.vidas_label = tk.Label(master, text=f"Vidas: {self.jogo.getVidas()}")
        self.vidas_label.pack(pady=10)

    def processar_palpite(self, event):
        palpite = self.entrada.get() # Pega o palpite
        if self.jogo.tentar(palpite):
            self.label.config(text='Parabéns!!!')
            self.entrada.config(state="disabled")
            self.vidas_label.config(text='Você acertou')
        else:
            self.entrada.delete(0, tk.END) # Limpa a entrada de texto
            self.vidas_label.config(text=f"Vidas: {self.jogo.getVidas()}")
        if self.jogo.getVidas() <= 0:
            self.label.config(text='Perdeu')
            self.entrada.config(state="disabled")
            self.vidas_label.config(text=f'a resposta era {self.jogo.getResposta()}')

while True:
    try:
        dificuldade = int(input("Digite a dificuldade: "))
        vida_inicial = int(input("Digite a quantidade de vida inicial: "))
        queda = int(input("Digite a quantidade de vida que irá perder quando errar: "))
        break
    except:
        print('Por favor, digite apenas números inteiros...')

# Passa os itens do txt para uma lista
with open("2023.02.28/Lista-de-Palavras.txt", "r") as arquivo:
    lista = arquivo.read().split()

root = tk.Tk()
jogo = Janela(root, JogoDoAnagrama, lista, dificuldade, vida_inicial, queda)
root.mainloop()