
"""
Created on 24/02/2023

@author: Luis Gustavo Caris dos Santos
"""

import tkinter as tk
from math import pi
val = 0

# Digita no display/executa o botão
def botao_clicado(valor):
    if 'ERROR' in display.get():
        texto_var.set('')
    if valor == '=':
        calcular()
    elif valor == 'AC':
        texto_var.set('')
    elif valor == 'C':
        texto_var.set(display.get()[:-1])
    elif valor == 'π':
        texto_var.set(display.get()+'pi')
    else:
        texto_var.set(display.get()+valor)

# Interpreta o calculo escrito no display
def calcular():
    try:
        texto_var.set(eval(display.get()))
        global val
        val = float(display.get())
    except:
        texto_var.set('ERROR')

# Cria a janela
calculadora = tk.Tk()
calculadora.title("Calculadora")
calculadora.resizable(False, False)

# Cria o display para digitar
texto_var = tk.StringVar()
display = tk.Entry(calculadora, width=20, font=('Arial', 16), justify='right', textvariable=texto_var)
display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Lista de rótulos para os botões
botoes = [
    'AC', 'C', 'val', 'π',
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Loop para criar os botões
linha = 1
coluna = 0
for texto in botoes:
    # Cria o botão
    botao = tk.Button(calculadora, text=texto, width=5, height=2, font=('Arial', 16), command=lambda valor=texto: botao_clicado(valor))
    # Adiciona o botão à grade
    botao.grid(row=linha, column=coluna, padx=5, pady=5)
    # Atualiza as coordenadas da grade
    coluna += 1
    if coluna > 3:
        linha += 1
        coluna = 0

# mostra a janela
calculadora.mainloop()