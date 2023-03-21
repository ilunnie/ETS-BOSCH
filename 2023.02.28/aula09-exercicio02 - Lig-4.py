
"""
Created on 28/02/2023

@author: Luis Gustavo Caris dos Santos
""""""
    Exercício 2 - Aula 9

Objetivo:
     • Crie um jogo de Lig-4 em python.

Regras:
     • Mostre para o usuário as posições das casas;
     • O game deve mostrar quando um jogador vencer ou quando der empate;
     • Deve possuir todo tipo de tratamento de erro, além de não permitir a jogada quando uma coluna estiver totalmente cheia;
     • O programa deve mostrar o diagrama do jogo e a cada rodada atualizar, mostrando em que casa os jogadores já jogaram;
     • Ao final de cada partida o programa mostra o vencedor, e pergunta se deseja continuar jogando.
"""

import tkinter as tk

class lig4():
    def __init__(self, player1, player2) -> None:
        self.jogadores = {'Jogador 1': player1, 'Jogador 2': player2}
        self.jogador_atual = list(self.jogadores.keys())[0]

    def setJogadorAtual(self):
        if self.jogador_atual == list(self.jogadores.keys())[0]:
            self.jogador_atual = list(self.jogadores.keys())[1]
        else:
            self.jogador_atual = list(self.jogadores.keys())[0]

    def getJogadorAtual(self):
        return self.jogador_atual

    def getCorAtual(self):
        return self.jogadores[self.jogador_atual]

class Janela(tk.Frame):
    def __init__(self, master=None, lig4=None):
        super().__init__(master)
        self.game = lig4
        self.master = master
        self.master.config(bg="black")  # Definir cor de fundo para preto
        self.master.title("Lig-4    |    By: Luis G. Caris") # Define o nome da janela
        self.master.resizable(False, False) # Deixa a janela fixa
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Cria o texto superior, que pode ser clicado
        self.clicked = False
        self.text_label = tk.Label(self, text=self.game.getJogadorAtual(), fg=self.game.getCorAtual(), cursor="hand2")
        self.text_label.bind("<Button-1>", self.jogarDeNovo)
        self.text_label.grid(row=0, column=0, columnspan=7)

        # Cria os botões
        self.buttons = []
        for i in range(7):
            button = tk.Button(self, text="{}".format(i+1), width=6, command=lambda num=i: self.clickButton(num))
            button.grid(row=1, column=i)
            self.buttons.append(button)

        self.reset()

    # Reinicia o tabuleiro quando clicar em "jogar de novo"
    def jogarDeNovo(self, event=None):
        None

    # Muda a cor do tabuleiro com base em coordenadas
    def setCor(self, x, y, cor):
        if x < 0 or x > 6 or y < 0 or y > 5:
            raise ValueError("Coordenadas fora do range permitido.")
        self.colors[x][y] = cor
        self.cells[y*7 + x].config(bg=cor)

    # Pega a cor de uma determinada area com base em coordenadas
    def getCor(self, x, y):
        if x < 0 or x > 6 or y < 0 or y > 5:
            raise ValueError("Coordenadas fora do range permitido.")
        return self.colors[x][y]

    # Coloca cor na coluna do botão clicado
    def clickButton(self, x):
        for y in range(len(self.colors[0])-1, -1, -1):
            if self.getCor(x, y) == 'black':
                self.setCor(x, y, self.game.getCorAtual())
                if self.verificar(x, y):
                    print(f'{self.game.getJogadorAtual()} ganhou!')
                    break
                self.game.setJogadorAtual()
                self.text_label.config(text=self.game.getJogadorAtual(), fg=self.game.getCorAtual())
                break

    # Verifica se ganhou
    def verificar(self, x, y):
        cor = self.getCor(x, y)
        self.sequencia = []

        # Verifica a vertical
        for i in range(5, 1, -1):
            if self.getCor(x, i) == cor and self.getCor(x, i-1) == cor and self.getCor(x, i-2) == cor and self.getCor(x, i-3) == cor:
                self.sequencia = [[x, i], [x, i-1], [x, i-2], [x, i-3]]
                return True

        # Verifica a horizontal
        for i in range(6, 2, -1):
            if self.getCor(i, y) == cor and self.getCor(i-1, y) == cor and self.getCor(i-2, y) == cor and self.getCor(i-3, y) == cor:
                self.sequencia = [[x, y], [x-1, y], [x-2, y], [x-3, y]]
                return True

        
    
    def reset(self):
        # Cria a tabela
        self.colors = [[0]*6 for _ in range(7)]
        self.cells = []
        for j in range(6):
            for i in range(7):
                color = "black"
                cell = tk.Frame(self, width=50, height=50, bg=color)
                cell.grid(row=j+2, column=i)
                self.colors[i][j] = color
                self.cells.append(cell)

# Pede as cores dos jogadores
def pedir_cores():
    cores_disponiveis = {'red', 'blue', 'green', 'white', 'yellow', 'purple', 'orange'}

    # Pedir a cor do jogador 1
    cor1 = None
    while not cor1:
        cor = input("Digite a cor do jogador 1: ").strip().lower()
        if cor in cores_disponiveis:
            cor1 = cor
            cores_disponiveis.remove(cor1)
        else:
            print("Cor inválida. Escolha entre:", ", ".join(sorted(cores_disponiveis)))

    # Pedir a cor do jogador 2
    cor2 = None
    while not cor2:
        cor = input("Digite a cor do jogador 2: ").strip().lower()
        if cor in cores_disponiveis:
            cor2 = cor
        else:
            print("Cor inválida ou já escolhida. Escolha entre:", ", ".join(sorted(cores_disponiveis)))

    return lig4(cor1, cor2)

# Cria a janela do jogo
jogo = pedir_cores()
root = tk.Tk()
app = Janela(master=root, lig4=jogo)
app.mainloop()