
"""
Created on 23/02/2023

@author: Luis Gustavo Caris dos Santos
"""

import random
import tkinter as tk

class JogoParImpar:
    def __init__(self, master):
        self.vitorias, self.derrotas, self.record, self.seguidas = 0, 0, 0, 0
        self.bot = 0
        
        self.frame_lado = tk.Frame(master)
        self.frame_lado.pack(side=tk.TOP)
        self.lbl_lado = tk.Label(self.frame_lado, text='Escolha PAR ou ÍMPAR:')
        self.lbl_lado.pack(side=tk.TOP)
        self.var_lado = tk.StringVar(value='PAR')
        self.rad_par = tk.Radiobutton(self.frame_lado, text='PAR', variable=self.var_lado, value='PAR')
        self.rad_par.pack(side=tk.LEFT)
        self.rad_impar = tk.Radiobutton(self.frame_lado, text='ÍMPAR', variable=self.var_lado, value='IMPAR')
        self.rad_impar.pack(side=tk.RIGHT)
        
        self.frame_mao = tk.Frame(master)
        self.frame_mao.pack(side=tk.TOP)
        self.lbl_mao = tk.Label(self.frame_mao, text='Digite um número de 1 a 10:')
        self.lbl_mao.pack(side=tk.TOP)
        self.var_mao = tk.StringVar()
        self.entry_mao = tk.Entry(self.frame_mao, textvariable=self.var_mao)
        self.entry_mao.pack(side=tk.BOTTOM)
        
        self.btn_jogar = tk.Button(master, text='Jogar', command=self.jogar)
        self.btn_jogar.pack(side=tk.TOP)
        
        self.frame_resultado = tk.Frame(master)
        self.frame_resultado.pack(side=tk.TOP)
        self.lbl_resultado = tk.Label(self.frame_resultado, text='')
        self.lbl_resultado.pack(side=tk.TOP)

        self.frame_scores = tk.Frame(master)
        self.frame_scores.pack(side=tk.BOTTOM)
        self.lbl_vitorias = tk.Label(self.frame_scores, text='Vitórias: {}'.format(self.vitorias))
        self.lbl_vitorias.pack(side=tk.LEFT)
        self.lbl_derrotas = tk.Label(self.frame_scores, text='Derrotas: {}'.format(self.derrotas))
        self.lbl_derrotas.pack(side=tk.LEFT)
        self.lbl_record = tk.Label(self.frame_scores, text='Record: {}'.format(self.record))
        self.lbl_record.pack(side=tk.LEFT)
    
    def jogada(self, mao):
        self.bot = random.randint(1, 10)
        if ((mao+self.bot)%2 == 0):
            resultado = 'PAR'
        else:
            resultado = 'ÍMPAR'
        self.resultado_jogada(resultado)
    
    def resultado_jogada(self, resultado):
        if (self.var_lado.get() == resultado):
            self.lbl_resultado.configure(text='Parabéns!!!\nVocê ganhou')
            self.vitorias += 1
            self.seguidas += 1
            if (self.seguidas > self.record):
                self.record = self.seguidas
        else:
            self.lbl_resultado.configure(text='Que pena...\nVocê perdeu')
            self.derrotas += 1
            self.seguidas = 0
        self.lbl_vitorias.configure(text='Vitórias: {}'.format(self.vitorias))
        self.lbl_derrotas.configure(text='Derrotas: {}'.format(self.derrotas))
        self.lbl_record.configure(text='Record: {}'.format(self.record))
        
    def jogar(self):
        try:
            mao = int(self.var_mao.get())
            if mao < 1 or mao > 10:
                raise ValueError('Valor inválido!')
            self.jogada(mao)
        except ValueError as e:
            self.lbl_resultado.configure(text=str(e))
    
if __name__ == '__main__':
    root = tk.Tk()
    root.title('Jogo Par ou Ímpar')
    root.geometry("300x175")
    root.resizable(width=False, height=False)
    jogo = JogoParImpar(root)
    root.mainloop()