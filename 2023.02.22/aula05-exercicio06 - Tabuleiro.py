
"""
Created on 22/02/2023

@author: Luis Gustavo Caris dos Santos
"""

# Importa o modulo tk da biblioteca tkinter
import tkinter as tk

# Cria a tabela
def cria_tabela(num):
    tabela = tk.Tk()
    tabela.title(f"Tabela ({num}x{num})")
    for i in range(num):
        for j in range(num):
            label = tk.Label(tabela, text="x", width=3, borderwidth=1, relief="solid")
            label.grid(row=i, column=j)
    tabela.mainloop()

# Loop que pede o tamanho da tabela sempre que fechada
while True:
    num = int(input("\nDigite o tamanho do tabuleiro: "))
    cria_tabela(num)